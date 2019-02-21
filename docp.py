from flask import Flask

from flask_peewee.admin import Admin
from flask_peewee.auth import Auth
from flask_peewee.db import Database

app = Flask(__name__)
db = Database(app)

# needed for authentication
auth = Auth(app, db)

# instantiate the Admin object for our project
admin = Admin(app, auth)