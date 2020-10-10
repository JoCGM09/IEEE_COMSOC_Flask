from flask import Flask
from views import routes_api

app = Flask(__name__)

app.register_blueprint(routes_api)

#MVT
#MODELO -> INFORMACION DE LA APP
#VISTA -> LOGICA DE LA APP
#TEMPLATE ->< UI

@app.route('/')
def hello():
    return "Hola mundo from Flask 32"

if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 4500, debug = True)