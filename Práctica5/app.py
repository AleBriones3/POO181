""" Importación del Framework """
from flask import Flask, render_template, request, redirect, url_for, flash

""" Importación de MySQL """
from flask_mysqldb import MySQL

""" Inicialización del APP """
app= Flask(__name__)

""" Configuración de la conexión """
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DBFlask'
app.secret_key='mysecretkey'
mysql=MySQL(app)

""" Declaración de la ruta, pertenece a http://localhost:5000  (El @app.route('/') es la ruta index o ruta principal)"""
@app.route('/') 
def index():
    CC= mysql.connection.cursor()
    CC.execute('select * from tb_albums')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums= conAlbums)

""" Ruta http:localhost:5000/guardar tipo POST para Insert """
""" "Methods" La ruta va a recibir información del formulario """
@app.route('/guardar', methods=['POST']) 
def Guardar():
    if request.method == 'POST':

        """ Pasamos a variables el contenido de los imputs """
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
      
        """ Conectar a la BD y ejecutar el insert """
        CS= mysql.connection.cursor()
        CS.execute('insert into tb_albums(titulo, artista, anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>') 
def Editar(id):
    cursorId= mysql.connection.cursor()
    cursorId.execute('SELECT * FROM tb_albums where id=%s',(id,))
    consultaId=cursorId.fetchone()
    return render_template('editarAlbum.html', Album=consultaId)

@app.route('/actualizar/<id>', methods=['POST']) 
def Actualizar(id):
    if request.method == 'POST':
        VARtitulo= request.form['txtTitulo']
        VARartista= request.form['txtArtista']
        VARanio= request.form['txtAnio']

        curAct= mysql.connection.cursor()
        curAct.execute('UPDATE tb_albums set titulo= %s, artista= %s, anio=%s WHERE id=%s',(VARtitulo, VARartista, VARanio, id))
        mysql.connection.commit()

    flash('Se actualizó el Album '+VARtitulo)
    return redirect(url_for('index'))

@app.route('/borrar/<id>') 
def Borrar(id):
    CursorId= mysql.connection.cursor()
    CursorId.execute('SELECT * FROM tb_albums where id=%s',(id,))
    ConsultaId=CursorId.fetchone()
    return render_template('eliminarAlbum.html', Album=ConsultaId)


@app.route('/eliminar/<id>', methods=['POST']) 
def Eliminar(id):
    if request.method == 'POST':
        vTitulo= request.form['txtTitulo']

        Cursorr= mysql.connection.cursor()
        Cursorr.execute('DELETE FROM tb_albums WHERE id=%s', (id,))
        mysql.connection.commit()

    flash('Se Eliminó el Album '+vTitulo)
    return redirect(url_for('index'))

""" Ejecución del servidor a través del puerto 5000 """
if __name__ == '__main__':
    app.run(port=5000,debug=True)
