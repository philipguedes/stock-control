import pprint
import datetime
from src.entities.clothes import Clothes
from flask import Flask, make_response, render_template, request
from src.firebase.firebase import Firebase


app = Flask(__name__, static_url_path='', static_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True
firebase = None
user = None


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    print('DEU CERTO PORRA')
    pprint.pprint(request.json)
    data = request.json
    email = data['email']
    password = data['password']
    firebase = Firebase()
    user = firebase.authenticate(email, password)
    print(user)
    return make_response("OK", 200)


@app.route('/stock-control', methods=['GET'])
def stock():
    print('HELLOOOOOOOOOOOOO')
    resp = make_response(render_template('stock/stock-window.html'), 200)
    pprint.pprint(resp)
    return resp


@app.route('/stock/newitem', methods=['POST'])
def create_new_item():
    # Verificar se estamos logado
    # Se sim, trader -> usuario logado
    trader = "teste"
    dateIn = datetime.datetime.now().timestamp()
    data = request.json
    link = data["link"]
    price = data["price"]
    cost = data["cost"]
    description = data["description"]

    # Criar objeto aqui
    cloth = Clothes(dateIn, trader, link, price, cost, description)
    # Salvar no firebase
    if firebase:
        firebase.create_new_cloth(cloth, user)


if __name__ == '__main__':
    app.run()
