from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
from routes.auth import routes_auth
from dotenv import load_dotenv

#from function_jwt import validate_token

app = Flask(__name__)
app.register_blueprint(routes_auth, url_prefix="/api")

#Me permite validar si el token generado es valido antes de ejecutar cualquier otra funcion, el problema es que hay una funcion para generar el token que no se ejecuta debido a esta funcion
#@app.before_request
#def verify_token_middleware():
#    token = request.headers['Authorization'].split(" ")[1]
#    return validate_token(token, output=False)

# La conexion para poder trabajar con la base de datos
conexion = MySQL(app)

# Ruta pedidos
@app.route('/mostrarEstado', methods=['GET'])
def mostrar_estados():
    """
    Me muestra todos los estados de los pedidos de la base de datos
    """

    try:
        # Crea una conexion con la base de datos
        cursor = conexion.connection.cursor()
        # Consulta sql
        sql="SELECT * FROM products"
        # Ejecuto la consulta
        cursor.execute(sql)
        # Obtengo los datos
        estado = cursor.fetchall()
        pedidos = []
        for i in estado:
            # Creating a dictionary with the data from the database.
            pedido={'numeroGuia':i[0],'numeroPedido':i[1],'estado':i[2],'lugar':i[3],'quienRecibe':i[4],'motivoDescripcion':i[5],'fecha':i[6],'hora':i[7],'link':i[8],'observacion':i[9]}
            # Appending the dictionary `pedido` to the list `pedidos`.
            pedidos.append(pedido)
        # Returning a JSON object with the key `pedidos` and the value `pedidos`.
        return jsonify({'pedidos':pedidos})

    except Exception as ex:
        # Returning a JSON object with the key `mensaje` and the value `Error`.
        return jsonify({'mensaje':"Error"})

@app.route('/mostrarEstado/<n_pedido>', methods=['GET'])
def mostra_pedido(n_pedido):
    """
    Me muestra el estado del numero de pedido que se le pasa por parametro
    
    :parametro n_guia: El numero de pedido que es unico
    """
    try:
        cursor = conexion.connection.cursor()
        # Consulta sql, el numero de pedido que se le pasa por parametro y se usa el format para que se pueda usar el parametro
        sql = "SELECT * FROM products WHERE numeroPedido = '{0}'".format(n_pedido)
        cursor.execute(sql)
        # el fetchone es para que solo me devuelva una fila(la que necesito segun el numero de pedido)
        datos = cursor.fetchone()
        # Creando un diccionario con los datos de la base de datos
        if datos != None:
            pedido={'numeroGuia':datos[0],'numeroPedido':datos[1],'estado':datos[2],'lugar':datos[3],'quienRecibe':datos[4],'motivoDescripcion':datos[5],'fecha':datos[6],'hora':datos[7],'link':datos[8],'observacion':datos[9]}
            return jsonify({'pedidos': pedido, 'mensaje': "Pedido encontrado."})
        else:
            return jsonify({'mensaje': "Pedido no encontrado."})

    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/trasmitirEstado', methods=['POST'])
def trasmitir_estado():
    """
    Me trasmite el estado del pedido a la base de datos
    """
    try:
        cursor = conexion.connection.cursor()
        # Obtengo los datos del json que se le pasa por parametro y los guardo en una variable
        sql = "INSERT INTO products (numeroGuia, numeroPedido, estado, lugar, quienRecibe, motivoDescripcion, fecha, hora, link, observacion) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}')".format(request.json['numeroGuia'], request.json['numeroPedido'], request.json['estado'], request.json['lugar'], request.json['quienRecibe'], request.json['motivoDescripcion'], request.json['fecha'], request.json['hora'], request.json['link'], request.json['observacion'])
        cursor.execute(sql)
        conexion.connection.commit() # Confirma la accion de insercion  
        return jsonify({'mensaje': "Estado del Pedido registrado..."})

    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/actualizarEstado/<n_pedido>', methods=['PUT'])
def actualizar_estado(n_pedido):
    """
    Me actualiza el estado del pedido en la base de datos
    
    :parametro n_pedido: El numero de pedido que es unico
    """
    try:
        cursor = conexion.connection.cursor()
        # Obtengo los datos del json que se le pasa por parametro y los guardo en una variable
        sql = "UPDATE products SET numeroGuia = '{0}', estado = '{1}', lugar = '{3}', quienRecibe = '{4}', motivoDescripcion = '{5}', fecha = '{6}', hora = '{7}', link = '{8}', observacion = '{9}' WHERE numeroPedido = '{2}'".format(request.json['numeroGuia'], request.json['estado'], request.json['lugar'], request.json['quienRecibe'], request.json['motivoDescripcion'], request.json['fecha'], request.json['hora'], request.json['link'], request.json['observacion'], n_pedido)
        cursor.execute(sql)
        conexion.connection.commit()  # Confirma la accion de insercion
        return jsonify({'mensaje': "Estado del Pedido actualizado..."})

    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/eliminarEstado/<n_pedido>', methods=['DELETE'])
def eliminar_estado(n_pedido):
    """
    Me elimina el estado del pedido que se le pasa por parametro
    
    :parametro n_guia: El numero de pedido que es unico
    """
    try:
        cursor = conexion.connection.cursor()
        # Obtengo los datos del json que se le pasa por parametro y los guardo en una variable
        sql = "DELETE FROM products WHERE numeroPedido = '{0}'".format(n_pedido)
        cursor.execute(sql)
        conexion.connection.commit()  # Confirma la accion de insercion
        return jsonify({'mensaje': "Estado del Pedido eliminado..."})

    except Exception as ex:
        return jsonify({'mensaje': "Error"})

def pagina_no_encontrada(error):
    """
    It returns a 404 error page
    
    :param error: The error that was raised
    """
    return "<h1>La pagina que intentas buscar no existe ... </h1>", 404

if __name__ == '__main__':
    # Cargar las variables de entorno
    load_dotenv()
    # Recurre al archivo configuracion y toma el parametro DEBUG = TRUE
    app.config.from_object(config['development'])
    # Manejador de errores, se le pasa como argumento el codigo de respuesta y la funcion
    app.register_error_handler(404, pagina_no_encontrada)
    # Inicia el servidor en el puerto 5000
    app.run(port=5000)
