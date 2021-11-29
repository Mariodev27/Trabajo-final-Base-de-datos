from pymysql import Connection
from pymysql.connections import Connection

from db import get_connection_db

#Creo una funcion para crear un empleado

def insert_employee(name, last_name, email, position):

    Connection=get_connection_db()

    with Connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO empleados(name, last_name, email, position) VALUES(%s, %s, %s, %s)",
            (name, last_name, email, position)
        )
    Connection.commit()
    Connection.close()

def get_employees():
    Connection = get_connection_db()
    # SELECT
    # creo un array de employees
    employees = []

    with Connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, last_name, email, position FROM empleados")
        employees = cursor.fetchall()
    Connection.close()

    return employees