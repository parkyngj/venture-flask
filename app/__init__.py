'''
Create the application object of class Flask, and then imports the views module.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Tell Flask to read and use our config file
app.config.from_object('config')

# Create db object that will be our database
db = SQLAlchemy(app)

from app import views, models
