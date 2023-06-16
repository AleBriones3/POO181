""" Importación del Framework """
from flask import Flask, render_template, request

""" Importación de MySQL """
from flask_mysqldb import MySQL

""" Inicialización del APP """
app= Flask(__name__)

""" Configuración de la conexión """
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DBFlask'
mysql=MySQL(app)

""" Declaración de la ruta, pertenece a http://localhost:5000  (El @app.route('/') es la ruta index o ruta principal)"""
@app.route('/') 
def index():
    return render_template('index.html')

""" Ruta http:localhost:5000/guardar tipo POST para Insert """
""" "Methods" La ruta va a recibir información del formulario """
@app.route('/guardar', methods=['POST']) 
def Guardar():
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        anio= request.form['txtAnio']
        print(titulo,artista,anio)
    return 'Los datos llegaron ;)'  

@app.route('/eliminar') 
def Eliminar():
    return "Se eliminó en la BD"

""" Ejecución del servidor a través del puerto 5000 """
if __name__ == '__main__':
    app.run(port=5000,debug=True)
