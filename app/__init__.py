'''
Create the application object of class Flask, and then imports the views module.
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

app = Flask(__name__)

# Tell Flask to read and use our config file
app.config.from_object('config')

# Create db object that will be our database
db = SQLAlchemy(app)

from app import views, models

lm = LoginManager()
lm.init_app(app)
# Flask-OpenID extension requires path to a temp folder where files can be stored
oid = OpenID(app, os.path.join(basedir, 'tmp'))
