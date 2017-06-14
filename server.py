from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/groups', methods=['GET', 'POST'] )
def index():
    if request.method == 'GET':
        return 'This is /groups'
    else:
        return 'This is /groups POST'
@app.route('/users/invite/<id>', methods=['POST'])
def send_invite(id):
    return 'Invite send to id: %s' % id

@app.route('/users/invite/accept/<group_id>', methods=['POST'])
def accept_invite(group_id):
    return 'Invite accepted from group_id: %s' % group_id

@app.route('/groups/<group_id>/user/<id>', methods=['DELETE'])
def remove_user_from_group(group_id, id):
    return 'User_id {} removed from group_id {}'.format(group_id, id)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)