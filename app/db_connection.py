import pymysql
from config.config import Config

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as err:
        print("Error al conectar a la base de datos:", err)
        return None