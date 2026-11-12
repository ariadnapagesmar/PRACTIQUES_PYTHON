# Nivell 7 al 8: Paràmetres i Peticions POST

# Exercici 7: Ruta amb paràmetre de URL (GET per ID)

# Objectiu: Consultar un element específic de la base de dades
# utilitzant la URL.
# Què has de fer: Crea una ruta a FastAPI del tipus
# @app.get("/vehicles/{vehicle_id}"). Quan l'usuari posi l'ID d'un vehicle,
# l'API ha de buscar-lo a la taula VEHICLES i retornar-ne les dades.
# Si no existeix, retorna un codi d'error 404.

# IMPORTEM FASTAPI I MYSQL
from fastapi import FastAPI, HTTPException
import mysql.connector

# FEM LA FUNCIÓ PER CONNECTAR-NOS A LA BD
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )

# FEM L'APP
app = FastAPI()

# FEM UN GET A /VEHICLES, PASSANT UN ID DE PARÀMETRE
@app.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    # CREEM LA CONNEXIÓ I EL CURSOR
    connexio = connectar_bd()
    cursor = connexio.cursor(dictionary=True)

    # FEM LA CONSULTA SQL I L'EXECUTEM ABANS DE GUARDAR ELS RESULTATS
    sql = "SELECT * FROM VEHICLES WHERE VEHICLE_ID = %s"
    cursor.execute(sql, (vehicle_id,))
    resultat = cursor.fetchone()

    # SI NO TROBA CAP RESULTAT, MOSTREM L'ERROR
    if not resultat:
        raise HTTPException(status_code=404, detail="Vehicle no trobat")

    # HO TANQUEM TOT
    cursor.close()
    connexio.close()

    # RETORNEM ELS RESULTATS
    return resultat

