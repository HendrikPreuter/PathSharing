from flask import Flask

app = Flask(__name__)

@app.route('/groups')
def index():
    return "dit is groep"