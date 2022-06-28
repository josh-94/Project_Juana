from flask import Flask, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL
from config import config

from routes.auth import routes_auth
from routes.rutas import rutas
from routes.ruta_auth import route_sharff
from routes.test import test_blueprint
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(routes_auth, url_prefix="/")
app.register_blueprint(rutas, url_prefix="/")
app.register_blueprint(route_sharff, url_prefix="/")
app.register_blueprint(test_blueprint, url_prefix="/test")

# La conexion para poder trabajar con la base de datos
conexion = MySQL(app)   

def pagina_no_encontrada(error):
    """
    Retorna una pagina de error cuando no se encuentra la pagina
    
    :param error: The error that was raised
    """
    #return "<h1>La pagina que intentas buscar no existe ... </h1>", 404
    return render_template('errors/404.html'), 404


def error_autorizacion(error):
    """
    Retorna una pagina de error al no tener autentificacion
    
    :param error: The error that was raised
    """
    #return "<h1>La pagina que intentas buscar no existe ... </h1>", 404
    return render_template('errors/405.html'), 405



if __name__ == '__main__':
    # Recurre al archivo configuracion y toma el parametro DEBUG = TRUE
    load_dotenv()
    # Registro la funcion pagina_no_encontrada como pagina de error
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(405, error_autorizacion)
    # Inicia el servidor en el puerto 5000
    isDev = getenv("JNB_ISDEV")
    if (isDev == "TRUE"):
        app.config.from_object(config['development'])
        #host = getenv("HOST", default="0.0.0.0")
        #port = getenv("PORT", default=5000)
        app.run(debug=True)
    else:
        app.config.from_object(config['production'])
        #host = getenv("HOST", default="0.0.0.0")
        #port = getenv("PORT", default=5000)
        app.run(debug=False)
