# Nivell 1 al 3: Python pur + Connexió a la Base de Dades (SQL)

# Exercici 1: El llistat bàsic (SELECT)

# Objectiu: Fer la teva primera consulta a Python per llegir dades.
# Què has de fer: Escriu un script en Python que es connecti a la teva
# base de dades local i faci un SELECT a la taula VEHICLES per mostrar
# per pantalla totes les matrícules i marques dels cotxes.

# IMPORTEM FASTAPI I EL MYSQL
from fastapi import FastAPI
import mysql.connector

# CREEM LA VARIABLE APP
app = FastAPI()

# INDIQUEM QUE VOLEM CONSULTAR (GET) EN LA TAULA VEHICLES
@app.get("/vehicles")

# CREEM LA FUNCIÓ QUE FA LA CONSULTA A LA BD
def llistar_vehicles():
    # OBRIM CONNEXIÓ AMB LA BD
    connexio = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )
    # ESCRIVIM EL DICTIONARY = TRUE PERQUÈ FACI QUE CADA FILA SIGUI UN
    # DICCIONARI EN LLOC D'UNA TUPLA. AIXÍ PASSA A SER JSON AUTOMÀTICAMENT
    cursor = connexio.cursor(dictionary=True)
    # FEM LA CONSULTA SELECT I GUARDEM ELS RESULTATS
    cursor.execute("SELECT MATRICULA, MARCA, MODEL FROM VEHICLES")
    resultats = cursor.fetchall()
    # HO TANQUEM TOT
    cursor.close()
    connexio.close()
    # RETORNEM ELS RESULTATS
    return resultats
