from flask import Flask, request, render_template, redirect

from controller import insert_employee, get_employees
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
