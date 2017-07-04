from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
db = create_engine("mysql+pymysql://root@localhost:3306/pathsharing")
connection = db.connect()
Session = sessionmaker(bind=db)
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(id='%s', username='%s', password='%s', email='%s')>" % (
            self.id, self.username, self.password, self.email)


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    admin = Column(String)
    name = Column(String)

    def __repr__(self):
        return "<User(id='%s', description='%s', admin='%s', name='%s')>" % (
            self.id, self.description, self.admin, self.name)

# TODO: figure out how CORS works exactly, possibly remove CORS(app) and add @cross_origin() where needed.
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'This is the homepage'})


@app.route('/groups/<id>', methods=['GET'])
def groups(id):
    session = Session()
    group = session.query(Groups).filter_by(id=id).one()
    session.close()
    return jsonify({
        'Group name': group.name,
        'Description': group.description
    })


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        session = Session()
        user = session.query(Users).filter_by(id='2').one()
        session.close()
        return jsonify({
                        'username': user.username,
                        'email': user.email
                        })
    else:
        return jsonify({'message': 'User added with ID: blablablaidk needs implementing'})


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return jsonify({'message': 'This is /about GET'})
    else:
        return jsonify({'message': 'This is /about POST'})


@app.route('/users/invite/<id>', methods=['POST'])
def send_invite(id):
    return jsonify({'message': 'Invite sent to id: ' + id})


@app.route('/users/invite/accept/<group_id>', methods=['POST'])
def accept_invite(group_id):
    return jsonify({'message': 'Invite accepted from group_id: ' + group_id})


@app.route('/groups/<group_id>/user/<id>', methods=['DELETE'])
def remove_user_from_group(group_id, id):
    return jsonify({'message': 'User_id ' + id + ' removed from group_id ' + group_id})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
