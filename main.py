from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_session import Session
app = Flask(__name__)
CORS(app)
app.config['CONFIG_HEADERS'] = 'Content-Type'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/submit/', methods=['GET'])
def getSubmit():
    response = {
        ''
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)