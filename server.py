from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# TODO: figure out how CORS works exactly, possibly remove CORS(app) and add @cross_origin() where needed.
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'message' : 'This is the homepage GET'})
    else:
        return jsonify({'message': 'This is the homepage POST'})


@app.route('/groups', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        return jsonify({'message' : 'This is /groups GET'})
    else:
        return jsonify({'message' : 'This is /groups POST'})


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify({'message' : 'This is /user GET'})
    else:
        return jsonify({'message' : 'This is /user POST'})


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return jsonify({'message' : 'This is /about GET'})
    else:
        return jsonify({'message' : 'This is /about POST'})


@app.route('/users/invite/<id>', methods=['POST'])
def send_invite(id):
    msg = 'Invite sent to id: ' + id
    return jsonify({'message': msg})


@app.route('/users/invite/accept/<group_id>', methods=['POST'])
def accept_invite(group_id):
    msg = 'Invite accepted from group_id: ' + group_id
    return jsonify({'message': msg})


@app.route('/groups/<group_id>/user/<id>', methods=['DELETE'])
def remove_user_from_group(group_id, id):
    msg = 'User_id ' + id + ' removed from group_id ' + group_id
    return jsonify({'message': msg})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
