import pyodbc

class Almacen_Bebidas:
    def __init__(self):
        # Especifica los detalles de la conexión a la base de datos
        server = 'ALE-BRIONES'
        database = 'ALMACEN_BEBIDAS'
        username = 'sa'
        password = 'Alebrije03'

        # Crea la cadena de conexión
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        try:
            # Establece la conexión
            self.connexion = pyodbc.connect(conn_str)
            self.cursor = self.connexion.cursor()

        except pyodbc.Error as e:
            print(f'Error de conexión: {str(e)}')

    def __del__(self):
        # Cierra el cursor y la conexión
        self.cursor.close()
        self.connexion.close()

    #MÉTODO INSERTAR BEBIDA
    def insertar_bebida_en_bd(self):
        print("Aquí se hace el registro de las bebidas")
        nombre = input("Ingresa el nombre: ")
        nombreClasificacion = input("Ingresa la clasificación: ")
        marca = input("Ingresa la marca: ")
        precio = input("Ingresa el precio de la bebida: ")
        self.cursor.execute("INSERT INTO ALTA_BEBIDAS VALUES (?, ?, ?, ?)", nombre, nombreClasificacion, marca, precio)
        self.cursor.commit()
        print("Tu registro fue exitoso")

    #MÉTODO ELIMINAR BEBIDA
    def eliminar_bebida_de_bd(self):
        print("Aquí se elimina un registro de las bebidas")
        id = input("Ingresa el id de la bebida: ")
        self.cursor.execute("DELETE FROM ALTA_BEBIDAS WHERE id=?", id)
        self.cursor.commit()
        print("Tu registro fue eliminado")

    #MÉTODO ACTUALIZAR DATOS DE LA  BEBIDA
    def actualizar_bebida_en_bd(self):
        print("Aquí se hace la actualización de las bebidas")
        id = input("Ingresa el ID de la bebida a actualizar: ")
        nombre = input("Ingresa el nombre: ")
        nombreClasificacion = input("Ingresa la clasificación: ")
        marca = input("Ingresa la marca: ")
        precio = input("Ingresa el precio de la bebida: ")
        self.cursor.execute("UPDATE ALTA_BEBIDAS SET nombre=? WHERE id=?", nombre, id)
        self.cursor.execute("UPDATE ALTA_BEBIDAS SET nombreClasificacion=? WHERE id=?", nombreClasificacion, id)
        self.cursor.execute("UPDATE ALTA_BEBIDAS SET marca=? WHERE id=?", marca, id)
        self.cursor.execute("UPDATE ALTA_BEBIDAS SET precio=? WHERE id=?", precio, id)

    # MÉTODO PARA CALCULAR EL PRECIO PROMEDIO DE LAS BEBIDAS
    def calcular_precio_promedio_bebidas(self):
        self.cursor.execute("SELECT AVG(precio) FROM ALTA_BEBIDAS")
        resultado = self.cursor.fetchone()[0]
        print(f"El precio promedio de las bebidas es: {resultado}")

    # MÉTODO PARA CALCULAR LA CANTIDAD DE BEBIDAS DE UNA MARCA
    def calcular_cantidad_bebidas_por_marca(self):
        marca = input("Ingresa el nombre de la marca: ")
        self.cursor.execute("SELECT COUNT(*) FROM ALTA_BEBIDAS WHERE marca=?", marca)
        resultado = self.cursor.fetchone()[0]
        print(f"La cantidad de bebidas de la marca {marca} es: {resultado}")

    # MÉTODO PARA CALCULAR LA CANTIDAD DE BEBIDAS POR CLASIFICACIÓN
    def calcular_cantidad_bebidas_por_clasificacion(self):
        clasificacion = input("Ingresa la clasificación: ")
        self.cursor.execute("SELECT COUNT(*) FROM ALTA_BEBIDAS WHERE nombreClasificacion=?", clasificacion)
        resultado = self.cursor.fetchone()[0]
        print(f"La cantidad de bebidas de la clasificación {clasificacion} es: {resultado}")

    #MÉTODO PARA SALIR DEL PROGRAMA
    def salir(self):
        print("Salir del Programa")
        exit()

#Main ----------------
def main():
    almacen_bebidas = Almacen_Bebidas()

    while True:
        print("             MENU          ")
        print("1.- Registrar bebida")
        print("2.- Eliminar bebida")
        print("3.- Actualizar bebidas")
        print("4.- Calcular precio promedio de las bebidas")
        print("5.- Calcular cantidad de bebidas por marca")
        print("6.- Calcular cantidad de bebidas por clasificación")
        print("7.- Salir")
        opcion = int(input("Opción: "))

        if opcion == 1:
            almacen_bebidas.insertar_bebida_en_bd()
        elif opcion == 2:
            almacen_bebidas.eliminar_bebida_de_bd()
        elif opcion == 3:
            almacen_bebidas.actualizar_bebida_en_bd()
        elif opcion == 4:
            almacen_bebidas.calcular_precio_promedio_bebidas()
        elif opcion == 5:
            almacen_bebidas.calcular_cantidad_bebidas_por_marca()
        elif opcion == 6:
            almacen_bebidas.calcular_cantidad_bebidas_por_clasificacion()
        elif opcion == 7:
            almacen_bebidas.salir()


if __name__ == '__main__':
    main()
