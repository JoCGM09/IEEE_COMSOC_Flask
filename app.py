from flask import Flask
from views import routes_api

app = Flask(__name__)

app.register_blueprint(routes_api)

@app.route('/')
def hello():
    return "hello world from flask"

if __name__ == '__main__':
    
    app.run(host = '0.0.0.0', port = 4500, debug = True)
