# Nivell 1: Connexió i Lectures bàsiques (READ)

# Exercici 1: Fes un script en Python que s'obri a la base de dades
# gestor_flota_db, faci un SELECT de tots els vehicles i mostri per la
# consola la seva marca i model amb un format net.

# IMPORTEM LA CONNEXIÓ SQL
import mysql.connector

# ESTABLIM LA CONNEXIÓ AMB LA BD
connexio1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
# CREEM EL CURSOR
cursor1 = connexio1.cursor()

# FEM LA CONSULTA I LA GUARDEM EN UNA VARIABLE 'RESULTATS'
cursor1.execute(
    "SELECT MARCA, MODEL, MATRICULA, ESTAT FROM VEHICLES"
)
resultats1 = cursor1.fetchall()

# OBRIM UN BUCLE FOR E IMPRIMIM UNA LLISTA AMB TOTS ELS VEHICLES
print("--- LLISTA VEHICLES ---")
for marca, model, matricula, estat in resultats1:
    print(f"{marca} --- {model} --- {matricula} --- {estat}")

# IMPORTANT TANCAR EL CURSOR I LA CONNEXIÓ
cursor1.close()
connexio1.close()

# Exercici 2: Modifica l'script anterior perquè llegeixi només els vehicles
# que estiguin en estat 'DISPONIBLE'.

# FEM LA CONNEXIÓ AMB LA BD
connexio2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
# CREEM EL CURSOR AMB LA CONNEXIÓ
cursor2 = connexio2.cursor()

# FEM LA CONSULTA SQL I GUARDEM ELS RESULTATS EN UNA VARIABLE
cursor2.execute("SELECT MARCA, MODEL, MATRICULA, ESTAT FROM VEHICLES WHERE ESTAT = 'DISPONIBLE'")
resultats2 = cursor2.fetchall()

# FEM UN BUCLE FOR E IMPRIMIM TOTS ELS VEHICLES DISPONIBLES
print("\n--- LLISTA VEHICLES DISPONIBLES ---")
for vehicle in resultats2:
    print(f"{vehicle[0]} --- {vehicle[1]} --- {vehicle[2]} --- {vehicle[3]}")

# IMPORTANT TANCAR EL CURSOR I LA CONNEXIÓ
cursor2.close()
connexio2.close()

# Exercici 3: Fes una consulta que compti el nombre total de conductors
# registrats i imprimeixi un missatge tipus: "Hi ha un total de X conductors
# a la base de dades".

# CONNECTEM EL PYTHON AMB LA BD
connexio3 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
# CREEM EL CURSOR
cursor3 = connexio3.cursor()

# FEM LA CONSULTA SQL I GUARDEM ELS RESULTATS EN UNA VARIABLE
cursor3.execute("SELECT COUNT(CONDUCTOR_ID) FROM CONDUCTORS")
resultats3 = cursor3.fetchall()

# IMPRIMIM EL NÚMERO DE CONDUCTORS EN LA BASE DE DADES
print(f"Hi ha un total de {resultats3[0][0]} conductors a la base de dades.")