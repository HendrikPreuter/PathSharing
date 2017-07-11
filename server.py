from flask import request, jsonify
from flask_cors import CORS
import gridfs
from modules import *

# TODO: figure out how CORS works exactly, possibly remove CORS(app) and add @cross_origin() where needed.
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'Lorem': 'ipsum homepage sit amet'
    })


@app.route('/about', methods=['GET'])
def about():
    return jsonify({'': 'Lorem ipsum dolor sit amet'})


@app.route('/user', methods=['GET', 'POST'])
def user_info():
    if request.method == 'GET':
        user = Users.query.filter_by(id='2').one()
        print(user.username)
        return jsonify({
            'username': user.username,
            'email': user.email
        })

    else:
        name = request.form['yourname']
        email = request.form['youremail']
        # return jsonify({'message:': 'User added with ID: blablablaidk needs implementing'})
        return jsonify({
            'Name': name,
            'Email': email
        })


@app.route('/users/invite/<id>', methods=['POST'])
def send_invite(id):
    return jsonify({'message': 'Invite sent to id: ' + id})


@app.route('/users/invite/accept/<group_id>', methods=['POST'])
def accept_invite(group_id):
    return jsonify({'message': 'Invite accepted from group_id: ' + group_id})


@app.route('/groups/<id>', methods=['GET'])
def groups(id):
    json = {}

    # Get all groups the user is in
    for useringroup in Users_has_Groups.query.filter_by(users_id=id).all():
        # Get the users that are in these groups
        group = Groups.query.filter_by(id=useringroup.groups_id).first()
        # Get the usernames of the users that are in the group and append them to the user list
        userlist = []
        for userid in Users_has_Groups.query.distinct().filter_by(groups_id=group.id).all():
            user = Users.query.filter_by(id=userid.users_id).first()
            userlist.append(user.username)
        # Now append the group name, description and users that are in the group to the JSON variable
        json[group.id] = {
            'name': group.name,
            'description': group.description,
            'members': userlist
        }

    print(json)
    return jsonify(json)

@app.route('/group/<int:user_id>', methods=['GET'])
def groupInfo(user_id):
    group = Groups.query.filter_by(id=user_id).first()

    userlist = []
    for userid in Users_has_Groups.query.distinct().filter_by(groups_id=group.id).all():
        user = Users.query.filter_by(id=userid.users_id).first()
        userlist.append(user.username)

    json = {
        'name': group.name,
        'description': group.description,
        'members': userlist
    }

    print(json)
    return jsonify(json)


@app.route('/groups/<group_id>/user/<id>', methods=['DELETE'])
def remove_user_from_group(group_id, id):
    return jsonify({'message': 'User_id ' + id + ' removed from group_id ' + group_id})


@app.route('/documents', methods=['POST'])
def addDocuments():

    #TODO: very basic, needs to be expanded upon
    filename = request.form['filename']
    #filename = "procedure.txt"
    mongo.save_file(filename, request.files['file'])

    return jsonify({'message':'File: ' + filename + ' has been saved!'})


@app.route('/documents/<filename>', methods=['GET', 'DELETE'])
def retrieveDocuments(filename):

    if request.method == 'GET':
        # Returns file
        return mongo.send_file(filename)
    else:
        # find file in MongoDB by filename
        file_info = mongo.db.fs.files.find_one({"filename": filename})
        file_id = file_info['_id']
        # Create gridFS object using mongo.db connection
        fs = gridfs.GridFS(mongo.db)
        # Delete all entries in the MongoDB with file_id
        fs.delete(file_id)

        return jsonify({'message': 'File: ' + filename + ' successfully deleted!'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
