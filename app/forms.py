'''
Web forms are represented in Flask-WTF as classes, subclassed from base class Form. A form subclass simply defines the fields of the form as class variables.

We create a login form that users will use to identify with the system. Login mechanism that we will support in our app is not the standard username/password type - we will have users login with their OpenID.

One benefit of using OpenID is that the authentication is done by the provider of the OpenID, so we don't have to validate passwords, which makes our site more secure to users.

OpenID login requires only one string (the so-called OpenID).
We also throw in a 'remember me' checkbox in the form, so that users can choose to have a cookie installed in their browsers that remembers their login when they come back.
'''

# Import Form class
from flask_wtf import Form
# Import the two form field classes we need
from wtforms import StringField, BooleanField
# Validator, a function that can be attached to a field to perform validation on data submitted by user
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
