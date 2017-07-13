from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/pathsharing'

app.config['MONGO_DBNAME'] = 'PathSharing'

db = SQLAlchemy(app)
mongo = PyMongo(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)


class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, unique=False)
    admin = db.Column(db.Integer, unique=False)
    name = db.Column(db.String(265), unique=True)


class Users_has_Groups(db.Model):
    __tablename__ = 'users_has_groups'
    pkey = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer)
    groups_id = db.Column(db.Integer)

class invitations(db.Model):
    __tablename__ = 'invitations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
