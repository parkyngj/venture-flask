# Local Setup Instructions

For my own reference.

- [Download](https://www.python.org/downloads/release/python-360/) Python 3.6.0
- Securely download `get-pip.py` from [here](https://pip.pypa.io/en/stable/installing/)
- Run `python3 get-pip.py`
- Run `pip3 install virtualenv`
- Run `virtualenv flask`
- Run `pip3 install Flask-WTF`
- Run `pip3 install sqlalchemy`
- Run `pip3 install sqlalchemy-migrate`
- Run `pip3 install six`
- Run `pip3 install sqlparse`
- Run `pip3 install Flask-Login`
  (handles user logged in state)
- Run `pip3 install Flask-OpenID`
  (provides user auth)


# Some SQLAlchemy Database Interactions

(To play with database from command-line.)

Run `python3`.

```python
# Brings database and models into memory
>>> from app import db, models

# Create a new user
>>> u = models.User(nickname='sally', email='sally@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```

Changes to database are done in context of a session. Multiple changes can be accumulated in a session and once all of the changes has been registered, we issue a single `db.session.commit()`.

If at any time working on a session there is an error, then a call to `db.session.rollback()` reverts the database to its state before the session was started.

```python
# Add another user
>>> u2 = models.User(nickname='susan', email='susan@example.com')
>>> db.session.add(u2)
>>> db.session.commit()

# Query for all users
>>> users = models.User.query.all()
>>> users # Returns [<User u'sally'>, <User u'susan'>]
>>> for u in users:
...     print(u.id,u.nickname)
...
1 sally
2 susan

# Another way to do queries: if we know id of user, we can find data for that user
u = models.User.query.get(1)
u # Returns <User u'sally'>

# Add a blog post
>>> import datetime
>>> u = models.User.query.get(1)
>>> p = models.Post(body="my first post!", timestamp=datetime.datetime.utcnow(), author=u)
>>> db.session.add(p)
>>> db.session.commit()

# Get all posts from a user
>>> u # Returns <User u'sally'>
>>> posts = u.posts.all()
>>> posts
[<Post u'my first post!'>]

# Obtain author of each post
>>> for p in posts:
...   print(p.id,p.author.nickname,p.body)
...
1 sally my first post!

# User 2 has no posts
>>> u2 = models.User.query.get(2)
>>> u # Returns <User u'susan'>
>>> u.posts.all()
[]

# Get all users in reverse alphabetical order
>>> models.User.query.order_by('nickname_desc').all()
[<User u'susan'>, <User u'sally'>]
```

See [Flask-SQLAlchemy] docs for learning about other options available to query database.

Can erase test users and posts we have created to clean database for further usage:

```python
>>> users = models.User.query.all()
>>> for u in users:
...   db.session.delete(u)
...
>>> posts = models.Post.query.all()
>>> for p in posts:
...   db.session.delete(p)
...
>>> db.session.commit()
```
