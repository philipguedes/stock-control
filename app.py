from flask import Flask, request, make_response
from src.services.firebase import Firebase

app = Flask(__name__, static_url_path='', static_folder='templates')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['passwrd']
    firebase = Firebase()
    try:
        user = firebase.authenticate(email, password)
        print(user)
        return make_response("OK", 200)
    except:
        return make_response("Failed", 404)
