# Nivell 5: El repte final (Gestió d'errors amb try/except)

import mysql.connector

connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# Exercici 10 (CRUD robust amb transaccions): Construeix un script que
# intenti inserir un nou conductor i, tot seguit, fer una acció incorrecta
# de manera intencionada (per exemple, inserir un registre duplicat o
# fallar a la sintaxi). Implementa una estructura try / except / rollback
# a Python de manera que si alguna cosa falla a la meitat, la base de
# dades faci un connexio.rollback() i desfaci tots els canvis per no
# deixar dades a mitges.

# FEM UN TRY. DINS FEM UN INSERT INTO CORRECTE, I UN ALTRE MALAMENT A POSTA
try:
    sql = "INSERT INTO CONDUCTORS (NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
    valors = ("Pili Margalef", "00000000A", 640404040)
    cursor.execute(sql, valors)
    connexio.commit()
    print("S'ha afegit el nou conductor correctament.")

    # FIQUEM EL MATEIX CARNET I NÚMERO DE TELÈFON QUE UN ALTRE CONDUCTOR
    # PER A QUE SALTI UN ERROR
    sql_error = "INSERT INTO CONDUCTORS(NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
    values = ("Alexia Pirau", "00000000A", 640404040)
    cursor.execute(sql_error, values)
    connexio.commit()
    print("S'ha afegit el nou conductor correctament.")
# EN CAS DE EXCEPTION, ENTRA AQUÍ DINS I MOSTRA L'ERROR
except mysql.connector.Error as error:
    print(f"S'ha produït un error: {error}")
    print("No s'ha pogut completar la comanda correctament.")
    # FEM UN ROLLBACK, PER A QUE LA BD QUEDI TAL QUAL ESTAVA ABANS DE
    # L'ÚLTIM COMMIT EFECTUAT CORRECTAMENT
    connexio.rollback()
    print("S'ha realitzat un rollback.")

