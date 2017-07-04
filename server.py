from flask import request, jsonify
from flask_cors import CORS
from modules import *


# TODO: figure out how CORS works exactly, possibly remove CORS(app) and add @cross_origin() where needed.
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'Lorem': 'ipsum homepage sit amet'
    })


@app.route('/groups/<id>', methods=['GET'])
def groups(id):
    group = Groups.query.filter_by(id=id).one()
    return jsonify({
        'Group name:': group.name,
        'Description:': group.description
    })


@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'GET':
        user = Users.query.filter_by(id='2').one()
        return jsonify({
                        'username:': user.username,
                        'email:': user.email
                        })
    else:
        return jsonify({'message:': 'User added with ID: blablablaidk needs implementing'})


@app.route('/about', methods=['GET'])
def about():
    return jsonify({'': 'Lorem ipsum dolor sit amet'})


@app.route('/users/invite/<id>', methods=['POST'])
def send_invite(id):
    return jsonify({'message:': 'Invite sent to id: ' + id})


@app.route('/users/invite/accept/<group_id>', methods=['POST'])
def accept_invite(group_id):
    return jsonify({'message:': 'Invite accepted from group_id: ' + group_id})


@app.route('/groups/<group_id>/user/<id>', methods=['DELETE'])
def remove_user_from_group(group_id, id):
    return jsonify({'message:': 'User_id ' + id + ' removed from group_id ' + group_id})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
