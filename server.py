from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/groups', methods=['GET', 'POST'] )
def index():
    if request.method == 'GET':
        return 'This is /groups'
    else:
        return 'This is /groups POST'

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)