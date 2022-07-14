from flask import Blueprint, jsonify, request
from flask_cors import CORS                             # El CORS debe estar en todos los archivos de ruta
from function_jwt import write_token, validate_token
#from function_validation import validar_password

routes_auth = Blueprint("routes_auth", __name__)
CORS(routes_auth)                                       # importante para origen cruzado

@routes_auth.route("/login", methods=["POST"])
def login():
    """
    Permite que el usuario genere al token para poder acceder a las rutas
    """
    data = request.get_json()
    if data['username'] == "UsuarioSharff":
        if data['password'] == "Sch@rff2022":
            return write_token(data=request.get_json())
        else:
            response = jsonify({"error": "Password incorrecto"})
            response.status_code = 401
            return response
        
        #if validar_password(data['password']):
            #return write_token(data=request.get_json())
        #else:
            #return jsonify({'Error': "La contraseña debe tener 8 digitos y no tener espacios."})
    else:
        response = jsonify({"message": "Usuario incorrecto"})
        response.status_code = 401
        return response

@routes_auth.route("/verifyToken", methods=["GET"])
def verifyToken():
    """
    Permite verificar el token, nos da como salida el usuario, password y tiempo de expiracion del token
    """
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)

