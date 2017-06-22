from flask import Flask, request, make_response
from flask_login import LoginManager, login_user, login_required
from src.services.firebase import Firebase
from src.services.login import UserClass

login_manager = LoginManager()
app = Flask(__name__, static_url_path='', static_folder='templates')
login_manager.init_app(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', None)
    password = data.get('password', None)
    firebase = Firebase()
    try:
        print(email)
        print(password)
        auth_data = firebase.authenticate(email, password)
        user = UserClass(auth_data)
        return make_response("OK", 200)
    except:
        raise
        return make_response("Failed", 404)


@login_manager.request_loader
def load_user_from_request(request):
    data = request.json
    email = data['email']
    password = data['password']
    firebase = Firebase()
    try:
        auth_data = firebase.authenticate(email, password)
        user = UserClass(auth_data)
        return user
    except:
        return None


@app.route('/teste', methods=['GET'])
@login_required
def teste():
    return make_response("I'M TESTE", 200)
