from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
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
        valors = (vehicle.matricula.upper().strip().replace(" ", ""), vehicle.marca.title().strip(),
                  vehicle.model.title().strip(), vehicle.estat, vehicle.quilometratge)

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

# EDITAR INFORMACIÓ D'UN VEHICLE
class VehicleUpdateModel(BaseModel):
    estat: EstatVehicle
    quilometratge: int

@app.put("/vehicles/{matricula}")
def editar_dades(matricula: str, dades: VehicleUpdateModel):
    connexio = None
    cursor = None

    try:
        connexio = connectar_bd()
        cursor = connexio.cursor()

        sql = "UPDATE VEHICLES SET ESTAT = %s, QUILOMETRATGE = %s WHERE MATRICULA = %s"
        cursor.execute(sql,(dades.estat, dades.quilometratge,
                            matricula.upper().strip().replace(" ", "")))
        connexio.commit()

        files_modificades = cursor.rowcount

        if files_modificades == 0:
            connexio.rollback()
            raise HTTPException(status_code=404, detail="Vehicle no trobat.")

    except mysql.connector.Error as e:
        connexio.rollback()
        raise HTTPException(status_code=500, detail=f"Error de servidor: {e}")

    finally:
        cursor.close()
        connexio.close()

    matricula_neta = matricula.upper().strip().replace(" ", "")
    return {"estat": "ok", "missatge": f"Vehicle amb matrícula {matricula_neta} actualitzat correctament"}

# DONAR DE BAIXA UN VEHICLE
@app.delete("/vehicles/{matricula}")
def eliminar_vehicle(matricula: str):
    connexio = None
    cursor = None

    try:
        connexio = connectar_bd()
        cursor = connexio.cursor()

        cursor.execute("DELETE FROM VEHICLES WHERE MATRICULA = %s",
                       (matricula.upper().strip().replace(" ", ""),))
        connexio.commit()

        files_eliminades = cursor.rowcount

        if files_eliminades == 0:
            raise HTTPException(status_code=404, detail="Vehicle no trobat.")

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error de servidor: {e}")

    finally:
        cursor.close()
        connexio.close()

    matricula_neta = matricula.upper().strip().replace(" ", "")
    return {"estat": "ok", "missatge": f"Vehicle amb matrícula {matricula_neta} eliminat correctament"}



