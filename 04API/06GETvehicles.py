# Exercici 6: Connectar FastAPI amb la BD (El GET de vehicles)

# Objectiu: Retornar dades reals de la base de dades a través
# d'una petició HTTP GET.
# Què has de fer: Modifica el teu main.py perquè la ruta
# @app.get("/vehicles") es connecti a la taula VEHICLES, faci un
# SELECT *, transformi el resultat a diccionari i el retorni en format JSON.

# IMPORTEM FASTAPI I MYSQL
from fastapi import FastAPI, HTTPException
import mysql.connector

# CONNECTEM AMB LA BD
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
# FEM EL CURSOR, I LI DIEM QUE HO PASSI TOT A DICCIONARI
cursor = connexio.cursor(dictionary=True)

# CREEM L'APP
app = FastAPI()

# FEM UN GET A /VEHICLES
@app.get("/vehicles")

# FEM UNA FUNCIÓ QUE MOSTRI TOTS ELS VEHICLES GUARDATS
def mostrar_vehicles():

    cursor.execute("SELECT * FROM VEHICLES")
    resultats = cursor.fetchall()

    # HO TANQUEM TOT
    cursor.close()
    connexio.commit()

    return resultats

