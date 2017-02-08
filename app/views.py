from flask import render_template, flash, redirect, session, url-for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
form .models import User

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')

def index():
    # Ensure that the page is seen only by logged in users
    @login_required
    # Pass g.user down to template, not dummy fake user
    user = g.user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                            title ='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
# Tell Flask-OpenID that this is our login view function
@oid.loginhandler
def login():
    # Check if there is a logged in user already, if so then we avoid doing a second login on top
    # g global is setup by Flask as a place to store and share data during the life of a request
        # (we store the logged in user here)
    if g.user is not None and g.user.is_authenticated:
        # url_for is defined by Flask as a clean way to obtain the URL for a given view function
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Distinction between flask.g object and flask.session (and distinction from db.session from Flask-SQLAlchemy)
        # Once data is stored in the session object, it will be available during that request and any future requests made by the same client.
        # Data remains in the session until explicitly removed
        # (To do this, Flask keeps a different session container for each client of our application)
        session['remember me'] = form.remember_me.data
        # Triggers user auth through Flask-OpenID
        # OpenID auth happens async - Flask-OpenID calls a function registered with oid.after_login decorator if authentication is successful
            # Else return user back to login page
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
        # flash('Login requested for OpenID="{}", remember_me="{}"'.format(form.openid.data, str(form.remember_me.data)))
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    # require valid email
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    # search database for email provided
    user = User.query.filter_by(email=resp.email).first()
    # if email not found, then consider as new user. Add new user to database
    if user is None:
        nickname = resp.nickname
        # handle case of missing nickname, since some openID providers may not have this info
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    # load remember_me value from Flask session
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    # call Flask-Login's login_user function to register as valid login
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
