# Exercici 10: Gestió completa de Reserves (L'API robusta)
import datetime

# Objectiu: Ajuntar relacions de taules i crear una reserva completa.

# Què has de fer: Crea una ruta @app.post("/reserves") que permeti registrar
# una nova reserva a la taula RESERVES vinculant un vehicle_id i un
# conductor_id. Opcionalment, afegeix una comprovació prèvia: si el vehicle
# ja té una reserva activa en aquelles dates, retorna un error impedint
# crear-la.

# IMPORTEM FASTAPI, MYSQL, PYDANTIC, DATETIME I ENUM
from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
import datetime
from enum import Enum

# FEM L'APP
app = FastAPI()

# FEM LA FUNCIÓ QUE ES CONNECTA A LA BD
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )

# CREEM UNA CLASSE ENUM PER A QUE A L'HORA DE CREAR LA NOVA RESERVA NOMÉS
# PUGUI FICAR UN D'AQUESTS TRES ESTATS
class EstatReserva(str, Enum):
    ACTIVA = "ACTIVA"
    PENDENT = "PENDENT"
    FINALITZADA = "FINALITZADA"

# FEM EL CONSTRUCTOR DE RESERVES AMB BASEMODEL
class ReservaModel(BaseModel):
    vehicle_id: int
    conductor_id: int
    data_inici: datetime.datetime
    data_fi: datetime.datetime
    estat_reserva: EstatReserva

# FEM UN POST A /RESERVES
@app.post("/reserves")
def reservar_vehicle(reserva: ReservaModel):

    # CREEM CONNEXIÓ I EL CURSOR
    connexio = connectar_bd()
    cursor = connexio.cursor()

    # FEM L'INSERT INTO A RESERVES
    sql = "INSERT INTO RESERVES (VEHICLE_ID, CONDUCTOR_ID, DATA_INICI, DATA_FI, ESTAT_RESERVA) VALUES (%s, %s, %s, %s, %s)"
    valors = (reserva.vehicle_id, reserva.conductor_id, reserva.data_inici, reserva.data_fi, reserva.estat_reserva)

    # FEM UN SELECT A VEHICLES PER COMPROVAR L'ESTAT DEL VEHICLE QUE ES VOL
    # FER LA RESERVA. EXECUTEM AQUESTA CONSULTA I GUARDEM EL RESULTAT
    sql_comprovacio = "SELECT ESTAT FROM VEHICLES WHERE VEHICLE_ID = %s"
    cursor.execute(sql_comprovacio, (reserva.vehicle_id,))
    resultat = cursor.fetchone()

    # SI EL RESULTAT NO ÉS 'OCUPAT'...
    if resultat[0] != "OCUPAT":
        # PODEM COMPROVAR SI PODEM EXECUTAR LA COMANDA DE L'INSERT INTO
        # I FER EL COMMIT. GUARDEM EL NOU ID DE RESERVES TAMBÉ
        try:
            cursor.execute(sql, valors)
            connexio.commit()

            nou_id = cursor.lastrowid
        # SI HI HA ALGUN ERROR A L'HORA DE CONNECTAR-SE AMB LA BD, FA
        # ROLLBACK I MOSTRA EL HTTPEXCEPTION
        except mysql.connector.Error as error:
            connexio.rollback()
            raise HTTPException(status_code=400, detail=f"Error de base de dades: {error}")
        # HI HAGI ERROR O NO A L'HORA DE CONNECTAR, HO TANCARÀ TOT
        finally:
            cursor.close()
            connexio.close()
        # I RETORNARÀ QUE TOT ESTÀ OK I EL NOU ID CREAT
        return {"estat": "ok", "missatge": f"Reserva creada amb ID: {nou_id}"}
    # SI EL VEHICLE TE L'ESTAT 'OCUPAT', MOSTREM UN MISSATGE D'ERROR I AVISEM
    # QUE AQUEST VEHICLE NO ES POT RESERVAR. TAMBÉ HO TANQUEM TOT
    else:
        cursor.close()
        connexio.close()
        return {"estat": "error", "missatge": f"El vehicle amb ID {reserva.vehicle_id} no es pot reservar"}
