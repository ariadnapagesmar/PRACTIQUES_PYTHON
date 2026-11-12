# Exercici 8: Enviar dades a l'API amb POST (Manteniments)

# Objectiu: Inserir dades a la base de dades fent una petició POST des de
# la documentació de FastAPI.

# Què has de fer: Crea una ruta @app.post("/manteniments") que rebi els
# detalls d'un nou manteniment (vehicle_id, descripció, cost, data) i
# l'insereixi a la taula MANTENIMENTS.

from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
import datetime

def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db",
    )

app = FastAPI()

class MantenimentModel(BaseModel):
    vehicle_id: int
    descripcio: str
    cost: float
    data_manteniment: datetime.date

@app.post("/manteniments")
def afegir_manteniment(manteniment: MantenimentModel):

    connexio = connectar_bd()
    cursor = connexio.cursor()

    sql = "INSERT INTO MANTENIMENTS (VEHICLE_ID, DESCRIPCIO, COST, DATA_MANTENIMENT) VALUES (%s, %s, %s, %s)"
    valors = (manteniment.vehicle_id, manteniment.descripcio, manteniment.cost, manteniment.data_manteniment)

    try:
        cursor.execute(sql, valors)
        connexio.commit()
        nou_id = cursor.lastrowid

    except mysql.connector.Error as error:
        connexio.rollback()
        raise HTTPException(status_code=400, detail=f"Error de base de dades: {error}")
    finally:
        cursor.close()
        connexio.close()

    return {"estat": "ok", "missatge": f"Manteniment afegit amb ID: {nou_id}"}