# Exercici 8: Enviar dades a l'API amb POST (Manteniments)

# Objectiu: Inserir dades a la base de dades fent una petició POST des de
# la documentació de FastAPI.

# Què has de fer: Crea una ruta @app.post("/manteniments") que rebi els
# detalls d'un nou manteniment (vehicle_id, descripció, cost, data) i
# l'insereixi a la taula MANTENIMENTS.

# IMPORTEM FASTAPI, MYSQL I PYDANTIC
from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
import datetime

# FEM LA FUNCIÓ QUE CONNECTA AMB LA BD
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db",
    )

# CREEM APP
app = FastAPI()

# FEM EL CONSTRUCTOR DE MANTENIMENTS
class MantenimentModel(BaseModel):
    vehicle_id: int
    descripcio: str
    cost: float
    data_manteniment: datetime.date

# FEM UN POST A /MANTENIMENTS DE LA BD
@app.post("/manteniments")
def afegir_manteniment(manteniment: MantenimentModel):

    # CREEM LA VARIABLE CONNEXIÓ I EL CURSOR
    connexio = connectar_bd()
    cursor = connexio.cursor()

    # FEM L'INSERT INTO A MANTENIMENTS AMB MYSQL
    sql = "INSERT INTO MANTENIMENTS (VEHICLE_ID, DESCRIPCIO, COST, DATA_MANTENIMENT) VALUES (%s, %s, %s, %s)"
    valors = (manteniment.vehicle_id, manteniment.descripcio, manteniment.cost, manteniment.data_manteniment)

    # PROVEM EXECUTAR LA CONSULTA I A FER EL COMMIT. GUARDEM EL NOU ID
    # GENERAT EN UNA VARIABLE
    try:
        cursor.execute(sql, valors)
        connexio.commit()
        nou_id = cursor.lastrowid

    # SI NO ES POT EXECUTAR LA COMANDA O FER EL COMMIT FA ROLLBACK I LLENÇA
    # UN EXCEPTION AMB L'ERROR
    except mysql.connector.Error as error:
        connexio.rollback()
        raise HTTPException(status_code=400, detail=f"Error de base de dades: {error}")
    # PASSI EL QUE PASSI HO TANQUEM TOT
    finally:
        cursor.close()
        connexio.close()

    # SI TOT VA BÉ, MOSTRARÀ UN OK I UN MISSATGE AMB EL NOU ID
    return {"estat": "ok", "missatge": f"Manteniment afegit amb ID: {nou_id}"}