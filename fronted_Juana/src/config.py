from distutils.debug import DEBUG
from os import getenv

class Config:
    SECRECT_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
# Modo de desarrollo
    DEBUG = True

    SERVER_NAME = getenv("JNB_SERVER_NAME", default="127.0.0.1:5001")

    # Credenciales para conectarse a la base de datos
    MYSQL_HOST = getenv("JNB_MYSQL_HOST", default="localhost") #''
    MYSQL_USER = getenv("JNB_MYSQL_USER", default='root')
    MYSQL_PASSWORD = getenv("JNB_MYSQL_PASSWORD", default='')
    MYSQL_DB = getenv("JNB_MYSQL_DB", default='')

class ProductionConfig():
    # Modo de desarrollo
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