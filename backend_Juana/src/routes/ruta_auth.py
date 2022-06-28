from flask import Blueprint, jsonify, request
from flask_cors import CORS
from function_jwt import validate_token
from function_validation import validar_nPedido
#from app import conexion

route_sharff = Blueprint("route_sharff", __name__)
CORS(route_sharff)

@route_sharff.before_request
def verify_token_middleware():
    """
    Token de autenticacion para poder acceder a las rutas 
    """
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=False)


@route_sharff.route('/trasmitirEstado', methods=['POST'])
def trasmitir_estado():
    """
    Permite el registro de informacion en la base de datos por parte de Sharff
    """

    headers = request.headers
    content = request.json #request.stream.read()
    grabarRawData(str(content), str(headers))

    # Valido que cumpla con tener "n" caracteres el numero de pedido
    if (validar_nPedido(request.json['numeroPedido'])):
        try:
            cursor = app.conexion.connection.cursor()
            # Obtengo los datos del json que se le pasa por parametro y los guardo en una variable
            sql = "INSERT INTO productos (numeroGuia, numeroPedido, estado, lugar, quienRecibe, motivoDescripcion, fecha, hora, link, observacion) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')".format(
                request.json['numeroGuia'], request.json['numeroPedido'], request.json['estado'], request.json['lugar'], request.json['quienRecibe'], request.json['motivoDescripcion'], request.json['fecha'], request.json['hora'], request.json['link'], request.json['observacion'])
            cursor.execute(sql)
            app.conexion.connection.commit() 
            return jsonify({'mensaje': "Se registró correctamente.", 'codigo': "1"})
        except Exception as ex:
            return jsonify({'mensaje': "Error"})
    else:
        return jsonify({'mensaje': "No se pudo registrar.", 'codigo': "0"})

def grabarRawData(header, content):
    try:
            cursor = app.conexion.connection.cursor()
            procedure = "usp_pedido_i_request"
            args = (header, content, 0);
            cursor.callproc(procedure, args)
            app.conexion.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            return False
