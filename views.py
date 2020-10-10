from flask import Blueprint

routes_api = Blueprint('routes_api', '__name__')



@app.route('/ruta1') #R
def hello(): #V
    return 'Hello world from flask Comsoc Ruta 1'

@app.route('/ruta2') #R
def hello(): #V
    return 'Hello world from flask Comsoc Ruta 2 '