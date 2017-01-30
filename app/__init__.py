'''
Create the application object of class Flask, and then imports the views module.
'''
from flask import Flask

app = Flask(__name__)

# Tell Flask to read and use our config file
app.config.from_object('config')

from app import views
