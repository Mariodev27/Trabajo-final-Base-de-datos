#Este archivo va a gestionar la conexión a la base de datos
import pymysql


def get_connection_db():
    return pymysql.connect(
        host='localhost',
        port=3309,
        user='root',
        password='',
        db='tecsup_empleados')
