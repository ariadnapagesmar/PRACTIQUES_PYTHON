# =====================================================================
# TEORIA CLAU: ARQUITECTURA DEL PROJECTE (API + BASE DE DADES)
# =====================================================================

# 1. QUÈ ÉS UNA API? (El patró client-servidor)
#
# Pensa en un restaurant:
#   - Tu (el client: la Web, l'App mòbil o l'M5Stack) fas una comanda.
#   - El cambrer (l'API de FastAPI) agafa la comanda i l'executa.
#   - La cuina (el backend amb Python + la Base de Dades MariaDB) prepara les dades.
#   - El cambrer et torna el plat (la resposta en format JSON).
#
# IMPORTANT: El client (mòbil/web) MAI parla directament amb la BD per seguretat.
# Tots els dispositius es comuniquen amb el mateix backend a través d'HTTP + JSON.


# 2. LES PARTS D'UNA PETICIÓ HTTP (Cap a l'API)
#
# 1. URL      -> on vas:          http://127.0.0.1:8000/vehicles/5
# 2. MÈTODE   -> què vols fer:    GET, POST, PUT, PATCH, DELETE
# 3. HEADERS  -> metadades:       Content-Type: application/json
# 4. BODY     -> dades que envies (només a POST/PUT/PATCH), en format JSON
#
# LA RESPOSTA de l'API té:
# 1. STATUS CODE -> com ha anat (200, 201, 404, 500...)
# 2. BODY        -> les dades que et retornen, normalment en JSON


# 3. LA TAULA SAGRADA: CRUD <-> SQL <-> MÈTODE HTTP
#
#   CRUD      SQL       MÈTODE HTTP   EXEMPLE D'URL (ENDPOINT)
#   Create    INSERT    POST          POST   /vehicles
#   Read      SELECT    GET           GET    /vehicles        (llistat)
#                                     GET    /vehicles/5      (un de concret)
#   Update    UPDATE    PUT / PATCH   PUT    /vehicles/5      (actualitzar)
#   Delete    DELETE    DELETE        DELETE /vehicles/5      (esborrar)
#
#   PUT   = substitueix l'objecte sencer
#   PATCH = modifica només alguns camps
#   L'URL és un NOM (recurs), i el MÈTODE HTTP és el VERB (l'acció).


# 4. EL FORMAT JSON
#
# És un text estructurat molt similar a un diccionari de Python:
#   {"matricula": "1234ABC", "marca": "Seat", "disponible": true, "km": 22000}
#
# Equivalències de tipus:
#   objecte {}   <->   dict de Python
#   array []     <->   llista de Python
#   true / null  <->   True / None de Python


# 5. STATUS CODES PRINCIPALS
#
#   2xx = Tot OK
#      200 OK          -> petició reeixida (GET, PUT)
#      201 Created     -> recurs creat correctament (POST)
#   4xx = Error del client (tu)
#      400 Bad Request -> dades mal formades
#      404 Not Found   -> no existeix el recurs demanat
#      409 Conflict    -> conflicte (ex: vehicle ja reservat)
#   5xx = Error del servidor (problema intern de Python/BD)
#      500 Internal Server Error


# =====================================================================
# COM ES CREA UNA API EN PYTHON AMB FASTAPI (El teu Servidor)
# =====================================================================
# Perquè la web, el mòbil i l'M5Stack puguin demanar coses, aixecaràs
# un servidor amb FastAPI i Uvicorn.
#
# INSTAL·LACIÓ: pip install fastapi uvicorn mysql-connector-python
# COMANDA PER ARRANCAR: uvicorn nom_del_fitxer:app --reload
# DOCUMENTACIÓ VISUAL: http://127.0.0.1:8000/docs
# =====================================================================

from fastapi import FastAPI, HTTPException
import mysql.connector

# Creació de l'objecte principal de l'API (obligatori)
app = FastAPI()


# Funció auxiliar per connectar a la teva base de dades local de XAMPP
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )


# =====================================================================
# EXEMPLES DE RUTES D'API CONNECTADES A LA TEVA BASE DE DADES
# =====================================================================

# 1. RUTA GET (Llegir tots els vehicles)
@app.get("/vehicles")
def llistar_vehicles():
    connexio = connectar_bd()
    cursor = connexio.cursor(dictionary=True)  # dictionary=True converteix files a diccionaris JSON

    cursor.execute("SELECT * FROM VEHICLES")
    resultat = cursor.fetchall()

    cursor.close()
    connexio.close()

    return resultat  # FastAPI converteix automàticament aquesta llista de dicts en JSON!


# 2. RUTA GET AMB PARÀMETRE (Llegir un vehicle per ID)
@app.get("/vehicles/{vehicle_id}")
def obtenir_vehicle_per_id(vehicle_id: int):
    connexio = connectar_bd()
    cursor = connexio.cursor(dictionary=True)

    sql = "SELECT * FROM VEHICLES WHERE VEHICLE_ID = %s"
    cursor.execute(sql, (vehicle_id,))
    vehicle = cursor.fetchone()  # Retorna només un registre

    cursor.close()
    connexio.close()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle no trobat")

    return vehicle


# 3. RUTA PUT (Actualitzar l'estat d'un vehicle - Ideal per l'M5Stack)
@app.put("/vehicles/{vehicle_id}/estat")
def actualitzar_estat_vehicle(vehicle_id: int, nou_estat: str):
    connexio = connectar_bd()
    cursor = connexio.cursor()

    sql = "UPDATE VEHICLES SET ESTAT = %s WHERE VEHICLE_ID = %s"
    cursor.execute(sql, (nou_estat, vehicle_id))
    connexio.commit()  # IMPORTANT en operacions d'escriptura (UPDATE/INSERT/DELETE)

    files_modificades = cursor.rowcount

    cursor.close()
    connexio.close()

    if files_modificades > 0:
        return {"estat": "ok", "missatge": f"Vehicle {vehicle_id} actualitzat a {nou_estat}"}
    else:
        raise HTTPException(status_code=404, detail="Vehicle no trobat per actualitzar")


# =====================================================================
# 3. RUTA POST (CREATE) AMB FASTAPI
# =====================================================================
# S'utilitza quan el client (web o mòbil) vol ENVIAR dades noves per crear
# un registre (per exemple, donar d'alta un nou conductor o crear una reserva).
#
# A FastAPI, fem servir models Pydantic o paràmetres directes per recollir
# les dades que arriben al cos (body) de la petició JSON.

from pydantic import BaseModel


# Definim com esperem que siguin les dades del nou conductor
class ConductorModel(BaseModel):
    nom: str
    carnet: str
    telefon: str


@app.post("/conductors", status_code=201)
def crear_conductor(conductor: ConductorModel):
    connexio = connectar_bd()
    cursor = connexio.cursor()

    sql = "INSERT INTO CONDUCTORS (NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
    valors = (conductor.nom, conductor.carnet, conductor.telefon)

    try:
        cursor.execute(sql, valors)
        connexio.commit()  # IMPORTANT: Guardar canvis a la BD (com un INSERT)
        nou_id = cursor.lastrowid  # Equivalent a recuperar l'ID autoincrementat
    except mysql.connector.Error as error:
        connexio.rollback()
        raise HTTPException(status_code=400, detail=f"Error de base de dades: {error}")
    finally:
        cursor.close()
        connexio.close()

    # Retornem un missatge i l'ID creat (equivalent al 201 Created)
    return {"estat": "ok", "conductor_id": nou_id, "missatge": "Conductor creat correctament"}


# =====================================================================
# 4. RUTES PUT (UPDATE) i DELETE (DELETE) AMB FASTAPI
# =====================================================================
# - PUT: Serveix per actualitzar un element existent (ex: modificar dades).
# - DELETE: Serveix per eliminar un element (ex: esborrar una reserva o manteniment).

@app.put("/manteniments/{manteniment_id}")
def actualitzar_manteniment_cost(manteniment_id: int, nou_cost: float):
    connexio = connectar_bd()
    cursor = connexio.cursor()

    sql = "UPDATE MANTENIMENTS SET COST = %s WHERE MANTENIMENT_ID = %s"
    cursor.execute(sql, (nou_cost, manteniment_id))
    connexio.commit()

    files_modificades = cursor.rowcount
    cursor.close()
    connexio.close()

    if files_modificades == 0:
        raise HTTPException(status_code=404, detail="Registre de manteniment no trobat")

    return {"estat": "ok", "missatge": f"Manteniment {manteniment_id} actualitzat amb èxit"}


@app.delete("/reserves/{reserva_id}", status_code=200)
def eliminar_reserva(reserva_id: int):
    connexio = connectar_bd()
    cursor = connexio.cursor()

    sql = "DELETE FROM RESERVES WHERE RESERVA_ID = %s"
    cursor.execute(sql, (reserva_id,))
    connexio.commit()

    files_esborrades = cursor.rowcount
    cursor.close()
    connexio.close()

    if files_esborrades == 0:
        raise HTTPException(status_code=404, detail="Reserva no trobada per eliminar")

    return {"estat": "ok", "missatge": f"Reserva {reserva_id} eliminada correctament"}

# =====================================================================
# 5. GESTIÓ D'ERRORS I EXCEPCIONS A FASTAPI
# =====================================================================
# Quan fas una API pròpia amb FastAPI, no fas servir "requests.raise_for_status()".
# En el seu lloc, fas servir la classe "HTTPException" de FastAPI per retornar
# el codi d'estat HTTP exacte (404, 400, 500) a la web o mòbil quan alguna cosa falla.
#
# Exemple dins d'una consulta:
#
#   if not vehicle:
#       raise HTTPException(status_code=404, detail="El vehicle no existeix a la flota")
#
# Si passa un error de connexió amb MariaDB (per exemple, XAMPP està tancat),
# pots capturar-ho amb try/except de Python:
#
#   try:
#       connexio = connectar_bd()
#   except mysql.connector.Error as err:
#       raise HTTPException(status_code=500, detail=f"Error de servidor de BD: {err}")

# El teu CRUD d’ara vs. el d’API

# Fixa’t que és gairebé el mateix que ja saps:

# El que ja saps (terminal):
#   connectar -> cursor -> execute -> fetchall -> print(...)
#
# Amb API (el mateix, però en lloc de print(...) fas return):
#   connectar -> cursor -> execute -> fetchall -> return resultat
#
# Només canvia que:
#  1. Escrius una línia (@app.get("/vehicles")) a sobre de la funció,
#     que vol dir: "quan algú visiti /vehicles, executa aquesta funció".
#  2. En comptes d'imprimir a la terminal, retornes el resultat
#     i FastAPI l'envia al navegador.

# Aquí tens l’esquelet, amb forats per omplir tu amb el teu CRUD de READ:

from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/vehicles")
def llistar_vehicles():
    # 1. connexio = ...      (el que ja saps)
    # 2. cursor = connexio.cursor(dictionary=True)
    # 3. cursor.execute(...) (un SELECT de VEHICLES)
    # 4. resultat = ...      (fetchall)
    # 5. tanca cursor i connexio
    # 6. return resultat     <- aquí és on abans feies print
    # ...

# El dictionary=True fa que cada fila sigui un diccionari
# ({"MATRICULA": "1234ABC", ...}) en lloc d’una tupla, i així es converteix a JSON sol.

# Passos concrets

# Posa l’esquelet de dalt en un fitxer main.py i omple els forats amb el teu
# CRUD de sempre.
# Engega XAMPP (MariaDB) i, a la terminal, dins la carpeta del fitxer:
# uvicorn main:app --reload
# Obre al navegador http://127.0.0.1:8000/vehicles. Hauries de veure els
# teus vehicles en JSON.