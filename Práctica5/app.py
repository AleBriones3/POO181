""" Importación del Framework """
from flask import Flask 

""" Importación de MySQL """
from flask_mysqldb import MySQL

""" Inicialización del APP """
app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DBFlask'
mysql=MySQL(app)

""" Declaración de la ruta, pertenece a http://localhost:5000  (El @app.route('/') es la ruta index o ruta principal)"""
@app.route('/') 
def index():
    return "Hola Mundo FLASK"

@app.route('/guardar') 
def Guardar():
    return "Se guardó en la BD"

@app.route('/eliminar') 
def Eliminar():
    return "Se eliminó en la BD"

""" Ejecución del servidor a través del puerto 5000 """
if __name__ == '__main__':
    app.run(port=5000,debug=True)
