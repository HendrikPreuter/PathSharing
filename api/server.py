import gridfs
from flask import jsonify
from flask_cors import CORS, cross_origin

from api.database.modules import *
from api.services.authenticator import *

CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'Lorem': 'ipsum homepage sit amet'
    })


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)

    try:
        user = Users.query.filter_by(username=data['username'])\
            .filter_by(password=data['password']).one()
        return jsonify({'token': generate_token(user)})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


@app.route('/about', methods=['GET'])
def about():
    return jsonify({'': 'Lorem ipsum dolor sit amet'})


@app.route('/user/<int:user_id>', methods=['GET'])
def user_info(user_id):
    print(user_id)
    if check_user():
        user = Users.query.filter_by(id=user_id).one()
        response = jsonify({
            'username': user.username,
            'email': user.email
        })
        print(response)
        return response


@app.route('/user', methods=['POST'])
def create_user_info():
    user_info = request.get_json(force=True)
    name = user_info['username']
    mail = user_info['email']
    password = user_info['password']
    user = Users(id=None, username=name, password=password, email=mail)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'response': 'success'
    })

@app.route('/invites', methods=['GET'])
def get_invites():
    user = get_user()
    userid= user['id']
    invitationslist = []
    for invitation in invitations.query.filter_by(user_id=userid).all():
        group = Groups.query.filter_by(id=invitation.group_id).first()
        invitationslist.append({'id': invitation.id,
                                'group_name': group.name,
                                'group_id': invitation.group_id,
                                'user_id': invitation.user_id})

    return jsonify(invitationslist)


@app.route('/invites', methods=['POST'])
def send_invite():
    data = request.get_json(force=True)
    username = data['user_name']
    groupname = data['group_name']
    groupinfo = Groups.query.filter_by(name=groupname).first()
    userinfo = Users.query.filter_by(username=username).first()
    invitation = invitations(id=None, user_id=userinfo.id, group_id=groupinfo.id)
    db.session.add(invitation)
    db.session.flush()
    db.session.commit()
    return jsonify({'response': 'succes'})


@app.route('/accept_invite', methods=['POST'])
def accept_invite():
    data = request.get_json(force=True)
    invitation = invitations.query.filter_by(id=data['invite_id']).first()
    db.session.delete(invitation)
    group = Users_has_Groups(pkey=None, users_id=data['user_id'], groups_id=data['group_id'])
    db.session.add(group)
    db.session.flush()
    db.session.commit()
    return jsonify({'response': 'succes'})


@app.route('/groups', methods=['GET'])
def groups():
    if check_user():
        user_info = get_user()
        id = user_info['id']
        grouplist = []
        # Get all groups the user is in
        for useringroup in Users_has_Groups.query.filter_by(users_id=id).all():

            # Get the users that are in these groups
            group = Groups.query.filter_by(id=useringroup.groups_id).first()

            # Get the name of the group admin
            groupadmin = Users.query.filter_by(id=group.admin).first()

            # Get the usernames of the users that are in the group and append them to the user list
            userlist = []
            for userid in Users_has_Groups.query.distinct().filter_by(groups_id=group.id).all():
                user = Users.query.filter_by(id=userid.users_id).first()
                userlist.append(user.username)
            # Now append the group name, description and users that are in the group to the JSON variable
            grouplist.append({
                'name': group.name,
                'id': group.id,
                'description': group.description,
                'admin': groupadmin.username,
                'members': userlist
            })

        json = {
            'response': 'succes',
            'groups': grouplist
        }
        return jsonify(json)


@app.route('/groups', methods=['POST'])
@cross_origin()
def create_group():
    if check_user():
        group_info = request.get_json(force=True)
        description = group_info['description']
        admin = group_info['admin']
        name = group_info['name']
        group = Groups(id=None, description=description, admin=admin, name=name)

        db.session.add(group)
        db.session.flush()
        groupid = group.id
        db.session.commit()


        users_has_groups = Users_has_Groups(pkey=None, users_id=admin, groups_id=groupid)
        db.session.add(users_has_groups)
        db.session.commit()
    return jsonify({
        'response': 'Group created successfully'
    })


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

    # TODO: very basic, needs to be expanded upon
    filename = request.form['filename']
    # filename = "procedure.txt"
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
    app.run(host='localhost', debug=True)
