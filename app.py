from flask import Flask, request, render_template, redirect
from pymysql import Connection
from pymysql import cursors
from pymysql.connections import Connection
from pymysql.cursors import Cursor
from controller import insert_employee, get_employees
from db import get_connection_db
#debo decirle a mi app que pueda cargar la carpeta
app=Flask(__name__, template_folder="templates")

#Esta es la ruta raiz
@app.route('/')
def home():
    employees = get_employees()
    return render_template('index.html', employees=employees)

@app.route('/crear')
def create():
    return render_template('create.html')

@app.route('/eliminar/<int:Id>')
def eliminar(Id):
    Connection=get_connection_db()
    Cursor.execute("DELETE from empleados WHERE Id=%s",(Id))
    Connection.commit()
    return redirect('/')

@app.route('/editar/<int:Id>')
def editar(Id):
    Connection=get_connection_db()
    Cursor.execute(
        "SELECT * FROM empleados WHERE Id=%s",(Id))
    employees = Cursor.fetchall()
    Connection.commit()
    print(employees)
    return render_template('empleados/editar.html',employees=employees)

@app.route('/registrarse')
def registrarse():
    employees = get_employees()
    return render_template('index2.html', employees=employees)

@app.route('/store-employee', methods=['POST'])
def store():
    name=request.form.get('name')
    last_name=request.form.get('last_name')
    email=request.form.get('email')
    position=request.form.get('position')

    insert_employee(name, last_name, email, position)
    return redirect('/')
    
#Vamos a inicializar nuestro servidor con flask
app.run(host='localhost', port=5000)
