# Nivell 4 al 6: Introducció a FastAPI (Els primers endpoints)
from click import password_option
# Exercici 4: Actualització de dades (UPDATE)

# Objectiu: Modificar un registre existent des de Python.
# Què has de fer: Escriu una funció que actualitzi el quilometratge d'un
# vehicle concret buscant-lo per la seva matrícula (MATRICULA). Recorda
# fer el commit()!

# IMPORTEM FASTAPI I EL MYSQL
from fastapi import FastAPI, HTTPException
import mysql.connector

# CONNECTEM AMB LA BD I FEM EL CURSOR
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# FEM L'APP
app = FastAPI()

# FEM EL PUT A /VEHICLES I PASSEM EL PARÀMETRE QUE BUSQUEM
@app.put("/vehicles({matricula}")
# FEM LA FUNCIÓ QUE ACTUALITZA ELS KM I PASSEM COM PARÀMETRES LA MATRÍCULA
# QUE BUSQUEM I EL NOU QUILOMETRATGE
def actualitzar_quilometratge(matricula: str, nou_quilometratge: int):

    # FEM EL UPDATE, EXECUTEM LA CONSULTA I FEM EL COMMIT
    sql = "UPDATE VEHICLES SET QUILOMETRATGE = %s WHERE MATRICULA = %s"
    cursor.execute(sql, (nou_quilometratge, matricula))
    connexio.commit()

    # GUARDEM EN UNA VARIABLE LES FILERES MODIFICADES ABANS DE TANCAR-HO TOT
    files_modificades = cursor.rowcount
    cursor.close()
    connexio.close()

    # SI NO S'HA MODIFICAT CAP FILERA, AVISEM QUE HI HA UN ERROR
    if files_modificades == 0:
        raise HTTPException(status_code=404, detail="Vehicle no trobat.")

    # RETORNEM UN MISSATGE DE QUE S'HA ACTUALITZAT CORRECTAMENT
    return {"estat": "ok", "missatge": f"El vehicle amb matrícula {matricula}"
                                       f"ha estat actualitzat amb èxit."}