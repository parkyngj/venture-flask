from flask import render_template, flash, redirect, session, url-for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
form .models import User

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Sally'} # fake user
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

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me="{}"'.format(form.openid.data, str(form.remember_me.data)))
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
