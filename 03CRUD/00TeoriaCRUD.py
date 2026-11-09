# L'estructura bàsica: Connexió

# Cada vegada que vulguis interactuar amb la base de dades des de Python,
# necessitaràs establir una connexió, crear un cursor (l'eina que "executa"
# les ordres SQL) i tancar-ho tot al final.

# 1. CREATE (Inserir dades)

# Per afegir un nou registre a una taula (per exemple, un nou vehicle).
# Fixa't que fem servir un %s per evitar atacs d'injecció SQL (passant les
# dades en una tupla a part).

import mysql.connector

# 1. Connectar a la base de dades
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",       # Posa la teva contrasenya si en tens
    database="gestor_flota_db"
)

cursor = connexio.cursor()

# 2. Instrucció SQL amb marcadors (%s)
sql = "INSERT INTO VEHICLES (MATRICULA, MARCA, MODEL, ESTAT, QUILOMETRATGE) VALUES (%s, %s, %s, %s, %s)"
valors = ("9999ZZZ", "Hyundai", "Tucson", "DISPONIBLE", 5000)

# 3. Executar la consulta
cursor.execute(sql, valors)

# IMPORTANT: En operacions que modifiquen dades (INSERT, UPDATE, DELETE),
# s'ha de fer un commit per guardar els canvis a la BD!
connexio.commit()

print(f"S'ha inserit el vehicle correctament. ID generat: {cursor.lastrowid}")

# 4. Tancar connexions
cursor.close()
connexio.close()

# 2. READ (Llegir / Consultar dades)

# Per recuperar informació. Aquí no cal fer commit() perquè no modifiquem
# res, només llegim. Utilitzem .fetchall() per portar-nos tots els resultats
# a Python.

import mysql.connector

connexio = mysql.connector.connect(
    host="localhost", user="root", password="", database="gestor_flota_db"
)
cursor = connexio.cursor()

# Executar una consulta de selecció
cursor.execute("SELECT MATRICULA, MARCA, MODEL, QUILOMETRATGE FROM VEHICLES WHERE ESTAT = 'DISPONIBLE'")

# Recuperar tots els resultats
resultats = cursor.fetchall()

print("--- VEHICLES DISPONIBLES ---")
for vehicle in resultats:
    # Cada vehicle és una tupla: (matricula, marca, model, quilometratge)
    print(f"Cotxe: {vehicle[1]} {vehicle[2]} ({vehicle[0]}) - {vehicle[3]} km")

# UN ALTRE MANERA MÉS FÀCIL DE FER EL BUCLE FOR AMB ELS RESULTATS DE LA CONSULTA
for matricula, marca, model, quilometratge in resultats:
    print(f"Cotxe: {matricula} {marca} {model} - {quilometratge} km")

cursor.close()
connexio.close()

# 3. UPDATE (Actualitzar dades)

# Per modificar dades existents (per exemple, canviar el quilometratge o
# l'estat d'un cotxe). Recorda el commit()!

import mysql.connector

connexio = mysql.connector.connect(
    host="localhost", user="root", password="", database="gestor_flota_db"
)
cursor = connexio.cursor()

# Actualitzem l'estat i els quilometratges d'un cotxe concret
sql = "UPDATE VEHICLES SET ESTAT = %s, QUILOMETRATGE = %s WHERE MATRICULA = %s"
valors = ('OCUPAT', 22000, '1234ABC')

cursor.execute(sql, valors)
connexio.commit()

print(f"Files modificades: {cursor.rowcount}")

cursor.close()
connexio.close()

# 4. DELETE (Esborrar dades)

# Per eliminar un registre de la base de dades (per exemple, esborrar un
# manteniment antic o una reserva cancel·lada). Compte sempre amb el WHERE
# o ho esborraràs tot!

import mysql.connector

connexio = mysql.connector.connect(
    host="localhost", user="root", password="", database="gestor_flota_db"
)
cursor = connexio.cursor()

sql = "DELETE FROM MANTENIMENTS WHERE MANTENIMENT_ID = %s"
valor = (4,) # Passem una tupla amb l'ID

cursor.execute(sql, valor)
connexio.commit()

print(f"S'han esborrat {cursor.rowcount} registres.")

cursor.close()
connexio.close()