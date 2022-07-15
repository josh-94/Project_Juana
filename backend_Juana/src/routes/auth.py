from flask import Blueprint, jsonify, request
from flask_cors import CORS                             # El CORS debe estar en todos los archivos de ruta
from function_jwt import write_token, validate_token
#from function_validation import validar_password
from time import strftime, localtime 
from datetime import datetime
routes_auth = Blueprint("routes_auth", __name__)
CORS(routes_auth)                                       # importante para origen cruzado

@routes_auth.route("/login", methods=["POST"])
def login():
    """
    Permite que el usuario genere al token para poder acceder a las rutas
    """
    list_validate = []
    time = strftime("%a, %d %b %Y %H:%M:%S GMT", localtime())           
    data = request.get_json()
    if data['username'] == "UsuarioSharff":
        if data['password'] == "Sch@rff2022":
            token = write_token(data=request.get_json())
            response1 = validate_token(token, output=True)
            for key, value in response1.items():
                if key != 'password':
                    list_validate.append(value)
            timestamp = datetime.utcfromtimestamp(list_validate[1])
            get_timestamp = timestamp.strftime('%a, %d %b %Y %H:%M:%S GMT')
            return jsonify({"access_token": token.decode("UTF-8"), "token_type": "bearer", "expires_in": list_validate[1], "userName": list_validate[0], ".issued": time, ".expires": get_timestamp})
        else:
            response = jsonify({"error": "Password incorrecto"})
            response.status_code = 401
            return response
     else:
        response = jsonify({"message": "Usuario incorrecto"})
        response.status_code = 401
        return response

@routes_auth.route("/verifyToken", methods=["POST"])
def verifyToken():
    """
    Permite verificar el token, nos da como salida el usuario, password y tiempo de expiracion del token
    """
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)

