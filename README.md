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

# Some SQLAlchemy Database Interactions

(To play with database from command-line.)

Run `python3`.

```python
# Brings database and models into memory
from app import db, models

# Create a new user
u = models.User(nickname='sally', email='sally@example.com')
db.session.add(u)
db.session.commit()
```

Changes to database are done in context of a session. Multiple changes can be accumulated in a session and once all of the changes has been registered, we issue a single `db.session.commit()`.

If at any time working on a session there is an error, then a call to `db.session.rollback()` reverts the database to its state before the session was started.

```python
# Add another user
u2 = models.User(nickname='susan', email='susan@example.com')
db.sessions.add(u2)
db.session.commit()

# Query for all users
users = models.User.query.all()
users # Returns [<User u'sally'>, <User u'susan'>]
>>> for u in users:
...     print(u.id,u.nickname)
...
1 sally
2 susan

# Another way to do queries: if we know id of user, we can find data for that user
u = models.User.query.get(1)
u # Returns <User u'sally'>

# Add a blog post
import datetime

```
