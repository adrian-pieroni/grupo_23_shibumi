from flask import Flask, render_template, request, url_for, jsonify, redirect 
#from flask_mysqldb import MySQL
from flask_cors import CORS
import mysql.connector
import random
from datetime import date

#Implementación de claves encriptadas

#CREAR Y GUARDAR EL ARCHIVO config.json con el siguiente formato:

#{
#  "api_key": "tu_clave_secreta_aqui",
#  "otra_clave": "otra_clave_secreta"
#}

#aquí comienza el proceso:

"""
from cryptography.fernet import Fernet
import json

def generar_clave_cifrado():
    return Fernet.generate_key()

def cifrar_claves(claves, clave_maestra):
    fernet = Fernet(clave_maestra)
    claves_cifradas = {clave: fernet.encrypt(valor.encode()) for clave, valor in claves.items()}
    return claves_cifradas

def descifrar_claves(claves_cifradas, clave_maestra):
    fernet = Fernet(clave_maestra)
    claves_descifradas = {clave: fernet.decrypt(valor).decode() for clave, valor in claves_cifradas.items()}
    return claves_descifradas

def cargar_claves():
    try:
        with open(`config.json`, `r`) as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("El archivo de configuración no se encontró.")
        return None

# Generar y guardar la clave maestra
clave_maestra = generar_clave_cifrado()

# Guardar claves cifradas en el archivo
claves = {"api_key": "tu_clave_secreta_aqui", "otra_clave": "otra_clave_secreta"}
claves_cifradas = cifrar_claves(claves, clave_maestra)

with open(`config.json`, `w`) as archivo:
    json.dump(claves_cifradas, archivo)

# Cargar y descifrar las claves
claves_cifradas = cargar_claves()
claves_descifradas = descifrar_claves(claves_cifradas, clave_maestra)

# Ejemplo de uso:
if claves_descifradas:
    api_key = claves_descifradas.get("api_key")
    otra_clave = claves_descifradas.get("otra_clave")

    # Aquí continúa tu código utilizando las claves
else:
    print("No se pueden cargar las claves.")
"""



app = Flask(__name__)
CORS(app) #ESTO HABILITA CORS PARA TODAS LAS RUTAS

# CLASE Registro
class Registro:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        self.cursor = self.conn.cursor()
        
        self.cursor.execute(f"USE `{database}`")
        
    def agregar_registrado(self, nombre, apellido, edad, calle, numero, ciudad, provincia, pais, codpos, tel, prefer):
        sql = "INSERT INTO `vpvejznx_ariatech`.`Registrados` (`nombre`, `apellido`, `edad`, `calle`, `numero`, `ciudad`, `provincia`, `pais`, `codpos`, `tel`, `prefer`)\
            VALUES (`" + nombre + "`, `" + apellido + "`, `" + edad + "`, `" + calle + "`, `" + numero + "`, `" + ciudad +\
                "`, `" + provincia + "`, `" + pais + "`, `" + codpos + "`, `" + tel + "`, `" + prefer + "`);"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return True
            
    def eliminar_registrado(self, id):
        sql = "DELETE FROM `vpvejznx_ariatech`.`Registrados` WHERE (`id` = '" + str(id) + "');"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_registrado_por_id(self, id):
        sql = "SELECT * FROM `vpvejznx_ariatech`.`Registrados` WHERE (`id` = '" + str(id) + "');"
        print(sql)
        self.cursor.execute(sql)
        registrado = self.cursor.fetchone()
        return registrado
        
    def modificar_registrado(self, id, nombre, apellido, edad, calle, numero, ciudad, provincia, pais, codpos, tel, prefer):
        sql = "UPDATE `vpvejznx_ariatech`.`Registrados` SET `nombre` = '" + nombre + "', `apellido` = '"\
            + apellido + "', `edad` = '" + edad + "', `calle` = '" + calle + "', `numero` = '"\
            + numero + "', `ciudad` = '" + ciudad + "', `provincia` = '" + provincia + "', `pais` = '"\
            + pais + "', `codpos` = '" + codpos + "', `tel` = '" + tel + "', `prefer` = '" + prefer + "' WHERE (`id` = '" + str(id) + "');"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_registrado(self): # ESTO ES UN METODO TIPO GET
        sql = "SELECT * FROM `vpvejznx_ariatech`.`Registrados`;"
        self.cursor.execute(sql) # ESTO EJECUTA LA CONSULTA
        registrado = self.cursor.fetchall() # ESTO DEVUELVE UNA LISTA DE TUPLAS
        return registrado
  
# FIN CLASE registro

####################################################
# PROGRAMA PRINCIPAL

registro = Registro(Datos de acceso a base de datos)

@app.route("/prueba", methods=["POST"]) #ESTO ES UN DECORADOR
def agregar_registrado():
    
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    edad = request.form["edad"]
    calle = request.form["calle"]
    numero = request.form["numero"]
    ciudad = request.form["ciudad"]
    provincia = request.form["provincia"]
    pais = request.form["pais"]
    codpos = request.form["codpos"]
    tel = request.form["tel"]
    prefer = request.form["prefer"]
            
    si_se_agrego = registro.agregar_registrado(nombre, apellido, edad, calle, numero, ciudad, provincia, pais, codpos, tel, prefer)
    if si_se_agrego:
        return jsonify({"mensaje": "registro agregado"}), 200 # ESTO ES UNA RESPUESTA HTTP OK
    else:
       return jsonify({"mensaje": "Error"}), 400 # ESTO ES UNA RESPUESTA HTTP ERROR

@app.route("/prueba", methods=["GET"])
def traer_registrado():
    registrados = registro.traer_registrado()
    return jsonify(registrados), 200 # ESTO ES UNA RESPUESTA HTTP OK

@app.route("/prueba/<int:id>", methods=["DELETE"])
def eliminar_registrado(id):
    registro_eliminado = registro.eliminar_registrado(id)
    if registro_eliminado:
        return jsonify({"mensaje": "producto eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

@app.route("/prueba/<int:id>", methods=["GET"])
def traer_registrado_por_id(id):
    registro_a = registro.traer_registrado_por_id(id)
    return jsonify(registro_a), 200

@app.route("/prueba/<int:id>", methods=["POST"])
def modificar_registrado(id):    
    
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    edad = request.form["edad"]
    calle = request.form["calle"]
    numero = request.form["numero"]
    ciudad = request.form["ciudad"]
    provincia = request.form["provincia"]
    pais = request.form["pais"]
    codpos = request.form["codpos"]
    tel = request.form["tel"]
    prefer = request.form["prefer"]
    
    si_se_modifico = registro.modificar_registrado(id, nombre, apellido, edad, calle, numero, ciudad, provincia, pais, codpos, tel, prefer)
    if si_se_modifico:
        return jsonify({"mensaje": "registro modificado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

if __name__ == "__main__":
    app.run(port=4000, debug=True)
