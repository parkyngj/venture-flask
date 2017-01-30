# Activates cross-site request forgery prevention
WTF_CSRF_ENABLED = True
# Create a cryptographic token that is used to validate a form
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Path of database file
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
# Folder where we store the SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
