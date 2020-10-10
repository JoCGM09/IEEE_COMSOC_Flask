from flask import Blueprint

routes_api = Blueprint('routes_api', __name__)


@routes_api.route('/ruta1')
def ruta1():
    return "hello world from flask ruta 1"

@routes_api.route('/ruta2')
def ruta2():
    return "hello world from flask ruta 2"