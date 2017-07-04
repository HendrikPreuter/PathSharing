from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

app = Flask(__name__)
# print(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/pathsharing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MONGO_DBNAME'] = 'PathSharing'

db = SQLAlchemy(app)
mongo = PyMongo(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)



class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, unique=False)
    admin = db.Column(db.String, unique=False)
    name = db.Column(db.String(265), unique=True)


class Users_has_Groups(db.Model):
    __tablename__ = 'users_has_groups'
    pkey = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.String)
    groups_id = db.Column(db.String)
