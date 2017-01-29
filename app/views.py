from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Sally'} # fake user
    return render_template('index.html',
                            title ='Home',
                            user=user)
