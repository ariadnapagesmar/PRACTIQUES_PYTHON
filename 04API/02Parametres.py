# Exercici 2: Filtres amb paràmetres (%s)

# Objectiu: Aprendre a filtrar dades de manera segura evitant injeccions SQL.

# Què has de fer: Programa una funció a Python a la qual li passis per
# paràmetre un estat (per exemple, 'DISPONIBLE' o 'EN TALLER')
# i et retorni només els vehicles que compleixen aquesta condició
# de la taula VEHICLES.

# IMPORTEM FASTAPI I MYSQL
from fastapi import FastAPI
import mysql.connector

# CREEM LA VARIABLE APP
app = FastAPI()

# FEM UN GET A /VEHICLES
@app.get("/vehicles")

# CREEM UNA FUNCIÓ QUE LI PASSEM PER PARÀMETRE L'ESTAT
def estat_vehicles(estat):

    # CONNECTEM AMB LA BD
    connexio = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )
    # FEM EL CURSOR AMB EL DICTIONARY=TRUE
    cursor = connexio.cursor(dictionary=True)

    # FEM LA CONSULTA SQL I L'EXECUTEM, PASSANT EL PARÀMETRE COM A TUPLA
    sql = ("SELECT MATRICULA, MARCA, MODEL, ESTAT FROM VEHICLES WHERE ESTAT = %s")
    cursor.execute(sql, (estat,))

    # GUARDEM ELS RESULTATS EN UNA VARIABLE
    resultats = cursor.fetchall()

    # HO TANQUEM TOT
    cursor.close()
    connexio.close()

    # RETORNEM ELS RESULTATS
    return resultats

