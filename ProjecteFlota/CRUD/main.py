from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flota_empresa_bd"
    )

# LLISTAR ELS VEHICLES
@app.get("/vehicles")
def llistar_vehicles():
    connexio = None
    cursor = None

    try:
        connexio = connectar_bd()
        cursor = connexio.cursor(dictionary=True)
        cursor.execute("SELECT * FROM VEHICLES")
        resultats = cursor.fetchall()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de servidor: {e}")
    finally:
        cursor.close()
        connexio.close()

    return resultats

# DONAR D'ALTA UN NOU VEHICLE
class EstatVehicle(str, Enum):
    DISPONIBLE = "DISPONIBLE"
    OCUPAT = "OCUPAT"
    EN_TALLER = "EN TALLER"
    INACTIU = "INACTIU"

class VehicleModel(BaseModel):
    matricula: str
    marca: str
    model: str
    estat: EstatVehicle
    quilometratge: int

@app.post("/vehicles")
def registrar_vehicle(vehicle: VehicleModel):
    connexio = None
    cursor = None

    try:
        connexio = connectar_bd()
        cursor = connexio.cursor(dictionary=True)

        sql = "INSERT INTO VEHICLES (MATRICULA, MARCA, MODEL, ESTAT, QUILOMETRATGE) VALUES (%s, %s, %s, %s, %s)"
        valors = (vehicle.matricula, vehicle.marca, vehicle.model, vehicle.estat, vehicle.quilometratge)

        cursor.execute(sql, valors)
        connexio.commit()
        nou_id = cursor.lastrowid

    except mysql.connector.Error as e:
        connexio.rollback()
        if e.errno == 1062:
            raise HTTPException(status_code=409, detail="Aquesta matrícula ja existeix a la base de dades")
        else:
            raise HTTPException(status_code=500, detail=f"Error de servidor: {e}")

    finally:
        cursor.close()
        connexio.close()

    return {"estat": "ok", "missatge": f"Vehicle afegit amb ID: {nou_id}"}

