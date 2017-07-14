import gridfs
from flask import jsonify
from flask_cors import CORS, cross_origin
import mimetypes

from api.database.modules import *
from api.services.authenticator import *

CORS(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)

    try:
        user = Users.query.filter_by(username=data['username']) \
            .filter_by(password=data['password']).one()
        return jsonify({
            'response': 'success',
            'token': generate_token(user)
        })
    except Exception as e:
        return jsonify({
            'response': 'error',
            'error': 'Invalid username or password',
            'debugging': str(e)
        })


@app.route('/user', methods=['GET'])
def user_info():
    if check_user():
        user = get_user()
        user_id = user['id']
        user = Users.query.filter_by(id=user_id).one()
        return jsonify({
            'username': user.username,
            'email': user.email
        })
    else:
        return jsonify({
            'response': 'error',
            'error': 'Incorrect username or password'
        })


@app.route('/user', methods=['POST'])
def create_user_info():
    user_info = request.get_json(force=True)
    name = user_info['username']
    email = user_info['email']
    password = user_info['password']
    try:
        if Users.query.filter_by(username=name).one():
            return jsonify({
                'response': 'error',
                'error': 'This username is already in use'
            })
    except:
        pass

    try:
        if Users.query.filter_by(email=email).one():
            return jsonify({
                'response': 'error',
                'error': 'This e-mail is already in use'
            })
    except:
        pass

    user = Users(id=None, username=name, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'response': 'success',
        'success': 'Account created successfully'
    })


@app.route('/invites', methods=['GET'])
def get_invites():
    user = get_user()
    user_id = user['id']
    invitations_list = []
    for invitation in invitations.query.filter_by(user_id=user_id).all():
        group = Groups.query.filter_by(id=invitation.group_id).first()
        invitations_list.append({
            'id': invitation.id,
            'group_name': group.name,
            'group_id': invitation.group_id,
            'user_id': invitation.user_id
        })
    if not invitations_list:
        return jsonify({
            'response': 'error',
            'error': 'You currently have no invitations'
        })
    return jsonify(invitations_list)


@app.route('/invites', methods=['POST'])
def send_invite():
    data = request.get_json(force=True)
    username = data['user_name']
    group_id = data['group_id']
    groupinfo = Groups.query.filter_by(id=group_id).first()
    if not groupinfo:
        return jsonify({
            'response': 'error',
            'error': 'There is no group with that name'
        })
    userinfo = Users.query.filter_by(username=username).first()
    if not userinfo:
        return jsonify({
            'response': 'error',
            'error': 'There is no user with username ' + username
        })
    if Users_has_Groups.query.filter_by(users_id=userinfo.id, groups_id=groupinfo.id).first():
        return jsonify({
            'response': 'error',
            'error': 'User ' + username + ' is already in that group'
        })
    if invitations.query.filter_by(user_id=userinfo.id, group_id=groupinfo.id).first():
        return jsonify({
            'response': 'error',
            'error': 'User ' + username + ' has already been invited to group that group'
        })
    invitation = invitations(id=None, user_id=userinfo.id, group_id=group_id)
    db.session.add(invitation)
    db.session.flush()
    db.session.commit()
    return jsonify({
        'response': 'success',
        'success': 'Invite has been sent'
    })


@app.route('/accept_invite', methods=['POST'])
def accept_invite():
    data = request.get_json(force=True)
    invitation = invitations.query.filter_by(id=data['invite_id']).first()
    db.session.delete(invitation)
    group = Users_has_Groups(pkey=None, users_id=data['user_id'], groups_id=data['group_id'])
    db.session.add(group)
    db.session.flush()
    db.session.commit()
    return jsonify({
        'response': 'success',
        'success': 'Invite has been accepted'
    })


@app.route('/groups', methods=['GET'])
def groups():
    if check_user():
        user_info = get_user()
        id = user_info['id']
        grouplist = []
        # Get all groups the user is in
        if not Users_has_Groups.query.filter_by(users_id=id).first():
            return jsonify({
                'response': 'error',
                'error': 'You are currently not in any group'
            })

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
            'response': 'success',
            'groups': grouplist
        }
        return jsonify(json)


@app.route('/groups', methods=['POST'])
@cross_origin()
def create_group():
    if check_user():
        group_info = request.get_json(force=True)
        print(group_info)
        description = group_info['description']
        admin = group_info['admin']
        name = group_info['name']
        try:
            if Groups.query.filter_by(name=name).one():
                return jsonify({
                    'response': 'error',
                    'error': 'This group name is already in use'
                })
        except:
            pass

        group = Groups(id=None, description=description, admin=admin, name=name)

        db.session.add(group)
        db.session.flush()
        groupid = group.id
        db.session.commit()

        users_has_groups = Users_has_Groups(pkey=None, users_id=admin, groups_id=groupid)
        db.session.add(users_has_groups)
        db.session.commit()
    return jsonify({
        'response': 'success',
        'success': 'Group created successfully'
    })


@app.route('/group/<int:group_id>', methods=['GET'])
def groupInfo(group_id):
    group = Groups.query.filter_by(id=group_id).first()

    userlist = []
    for userid in Users_has_Groups.query.distinct().filter_by(groups_id=group_id).all():
        user = Users.query.filter_by(id=userid.users_id).first()
        userlist.append(user.username)

    json = {
        'name': group.name,
        'description': group.description,
        'members': userlist,
        'admin': group.admin
    }
    print(json)
    return jsonify(json)


@app.route('/documents', methods=['POST'])
def addDocuments():
    # print('we"re in addDocuments()')
    try:
        fs = gridfs.GridFS(mongo.db)

        file = request.files['file']
        group_id = request.form['group_id']
        filename = file.filename
        content_type = mimetypes.guess_type(filename)[0]

        store = fs.put(file, content_type=content_type, filename=filename, groupId=group_id)

        return jsonify({
            'response': 'success',
            'success': 'File was successfully uploaded'
        })
    except Exception as e:
        print(str(e))
        return jsonify({
            'response': 'error',
            'error': str(e)
        })


@app.route('/documents/<groupId>', methods=['GET'])
def retrieveDocuments(groupId):
    # Returns file
    #return mongo.send_file(filename)
    files = []

    documents = mongo.db.fs.files.find({"groupId": groupId})

    for document in documents:
        files.append(document['filename'])

    #print(files)

    json = {
        'response': 'succes',
        'files': files
    }

    return jsonify(json)

@app.route('/document/<filename>', methods=['GET'])
def getFile(filename):
    return mongo.send_file(filename)



@app.route('/documents/<filename>', methods=['DELETE'])
def removeDocuments(filename):
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
