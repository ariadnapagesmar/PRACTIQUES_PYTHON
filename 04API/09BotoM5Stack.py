# Nivell 9 al 10: Escenaris reals del projecte
# (L'M5Stack i Reserves)

# Exercici 9: Simulació del botó de l'M5Stack (Check-out)

# Objectiu: Crear una petició PUT per canviar l'estat d'un vehicle (simulant
# quan algú s'emporta les claus).
# Què has de fer: Fes una ruta @app.put("/vehicles/{vehicle_id}/checkout")
# que actualitzi l'estat d'aquell vehicle a 'OCUPAT' a la taula VEHICLES i
# retorni un missatge de confirmació. Aquesta és la lògica exacta que farà
# servir l'aparell físic!

# IMPORTEM FASTAPI I MYSQL
from fastapi import FastAPI, HTTPException
import mysql.connector

# CREEM APP
app = FastAPI()

# FEM LA FUNCIÓ QUE ES CONNECTA A LA BD
def connectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestor_flota_db"
    )

# FEM UN PUT A /VEHICLES, PASSANT-LI UN PARÀMETRE {VEHICLE_ID} I LI POSEM
# DE NOM CHECKOUT
@app.put("/vehicles/{vehicle_id}/checkout")
# FEM LA FUNCIÓ QUE CANVIA L'ESTAT DEL VEHICLE A 'OCUPAT'
def fer_checkout_vehicle(vehicle_id: int):

    # CREEM CONNEXIÓ I CURSOR
    connexio = connectar_bd()
    cursor = connexio.cursor()

    # FEM LA COMANDA SQL
    sql = "UPDATE VEHICLES SET ESTAT = %s WHERE VEHICLE_ID = %s"

    # INTENTEM EXECUTAR LA COMANDA I FER EL COMMIT, GUARDANT EL ROWCOUNT
    try:
        cursor.execute(sql, ("OCUPAT", vehicle_id))
        connexio.commit()

        files_modificades = cursor.rowcount
    # SI SALTA ERROR, FA ROLLBACK I EL MOSTRA
    except mysql.connector.Error as error:
        connexio.rollback()
        print(f"{error}. No s'ha pogut modificar l'estat del vehicle.")
    # PASSI EL QUE PASSI, HO TANQUEM TOT
    finally:
        cursor.close()
        connexio.close()

    # SI NO S'HA MODIFICAT CAP FILA, MOSTRA L'ERROR 404: NO EXISTEIX EL
    # RECURS DEMANAT
    if files_modificades == 0:
        raise HTTPException(status_code=404, detail="Vehicle no trobat")

    # RETORNEM QUE TOT ESTÀ BÉ I LES FILES MODIFICADES
    return {"estat": "ok", "missatge": f"Estat modificat amb èxit. "
                                       f"Files modificades: {files_modificades}"}