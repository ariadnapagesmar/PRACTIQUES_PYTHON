# Exercici 3: Inserció de dades (INSERT + commit)

# Objectiu: Entendre la importància del commit() en les escriptures.

# Què has de fer: Fes un script que insereixi un nou conductor a la taula
# CONDUCTORS (passant-li nom, carnet i telèfon). Comprova a phpMyAdmin
# que s'ha guardat correctament.

# IMPORTO FASTAPI, MYSQL I BASEMODEL PER PODER FER AFEGIR DADES A LA BD AMB POST
from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

# FEM L'APP
app = FastAPI()

# CREEM UNA FUNCIÓ QUE BÀSICAMENT ÉS PER CONNECTAR AMB LA BD
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )

# FEM UN CONSTRUCTOR AMB LES DADES QUE VOLEM AFEGIR A LA BD
class ConductorModel(BaseModel):
    nom: str
    carnet: str
    telefon: str

# FEM UN POST A /CONDUCTORS
@app.post("/conductors")
def crear_conductor(conductor: ConductorModel):
    # CRIDEM LA FUNCIÓ PER CONNECTAR-NOS A LA BD I FEM EL CURSOR
    connexio = connectar_bd()
    cursor = connexio.cursor()

    # FEM LA CONSULTA SQL I GUARDEM ELS VALORS EN UN ALTRE VARIABLE
    sql = "INSERT INTO CONDUCTORS (NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
    valors = (conductor.nom, conductor.carnet, conductor.telefon)

    # PROVEM EXECUTAR LA COMANDA I FER EL COMMIT
    try:
        cursor.execute(sql, valors)
        connexio.commit()
        nou_id = cursor.lastrowid
    # SI ALGUNA COSA VA MALAMENT, FA ROLLBACK I MOSTRA L'ERROR
    except mysql.connector.Error as error:
        connexio.rollback()
        raise HTTPException(status_code=400, detail=f"Error de base de dades: {error}")
    # PASSI EL QUE PASSI, HO TANQUEM TOT
    finally:
        cursor.close()
        connexio.close()

    # RETORNEM QUE TOT HA ESTAT BÉ EN FORMAT JSON, ENSENYANT TAMBÉ EL NOU ID
    return {"estat": "ok", "missatge": f"Conductor creat amb ID: {nou_id}"}