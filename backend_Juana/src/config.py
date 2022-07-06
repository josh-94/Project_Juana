from os import getenv

# Configuraciones del proyecto

class DevelopmentConfig():
    # Modo de desarrollo
    DEBUG = True 

    SERVER_NAME = getenv("JNB_SERVER_NAME", default="0.0.0.0:5000")

    # Credenciales para conectarse a la base de datos
    MYSQL_HOST = getenv("JNB_MYSQL_HOST", default="localhost") #''
    MYSQL_USER = getenv("JNB_MYSQL_USER", default='root')
    MYSQL_PASSWORD = getenv("JNB_MYSQL_PASSWORD", default='')
    MYSQL_DB = getenv("JNB_MYSQL_DB", default='')

class ProductionConfig():
    # Modo de produccion
    DEBUG = False 

    #SERVER_NAME = getenv("JNB_SERVER_NAME", default="0.0.0.0:5000")

    # Credenciales para conectarse a la base de datos
    MYSQL_HOST = getenv("JNB_MYSQL_HOST", default="localhost") #''
    MYSQL_USER = getenv("JNB_MYSQL_USER", default='root')
    MYSQL_PASSWORD = getenv("JNB_MYSQL_PASSWORD", default='')
    MYSQL_DB = getenv("JNB_MYSQL_DB", default='')
 
config={
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

