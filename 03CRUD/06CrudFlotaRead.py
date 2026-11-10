# Nivell 1: Consultes (READ) amb filtres i paràmetres

# IMPORTEM EL MYSQL
import mysql.connector
# FEM LA CONNEXIÓ AMB LA BD I CREEM EL CURSOR
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# Exercici 1: Fes un script en Python que demani a l'usuari una marca per
# teclat (input()) i mostri per pantalla tots els vehicles d'aquella marca
# (matrícula, model i quilometratge).

# GUARDEM EN UNA VARIABLE LA MARCA QUE ESCRIU L'USUARI PER CONSOLA
marca = input("Escriu una marca per cercar vehicles en el registre: ").title()
# FEM LA CONSULTA SQL: QUE MOSTRI TOTS ELS VEHICLES DE LA MARCA GUARDADA
sql = "SELECT MATRICULA, MARCA, MODEL, QUILOMETRATGE FROM VEHICLES WHERE MARCA = %s"
valor = (marca,)
# EXECUTEM LA CONSULTA I GUARDEM ELS RESULTATS
cursor.execute(sql, valor)
resultats1 = cursor.fetchall()

# FEM UN BUCLE FOR QUE MOSTRI TOTS ELS VEHICLES DE LA MARCA EN QÜESTIÓ
for matricula, marca, model, quilometratge in resultats1:
    print(f"{matricula} - {marca} {model} - {quilometratge}")

# Exercici 2: Escriu un script que llegeixi tots els manteniments registrats
# a la taula MANTENIMENTS i calculi i imprimeixi per consola el cost total
# de tots els tallers junts.

print("--- GASTOS TOTALS EN MANTENIMENTS ---")
# FEM LA CONSULTA SQL: QUE SUMI TOTS ELS COSTOS DE LA TAULA DE MANTENIMENTS
# I GUARDEM ELS RESULTATS
cursor.execute("SELECT SUM(COST) FROM MANTENIMENTS")
resultats2 = cursor.fetchall()

# MOSTREM PER CONSOLA LA SUMA TOTAL
print(f"Suma total de tots els manteniments: {resultats2[0][0]} euros")

# Exercici 3: Fes una consulta que mostri el nom i el telèfon de tots els
# conductors que tinguin una reserva amb l'estat 'PENDENT'.

# FEM LA CONSULTA SQL: QUE MOSTRI LES DADES DELS CONDUCTORS QUE TENEN UNA
# RESERVA EN ESTAT DE PENDENT, I GUARDEM ELS RESULTATS
cursor.execute("SELECT NOM, TELEFON, ESTAT_RESERVA FROM CONDUCTORS JOIN RESERVES USING (CONDUCTOR_ID) WHERE ESTAT_RESERVA = 'PENDENT'")
resultats3 = cursor.fetchall()

# FEM UN FOR QUE MOSTRI EL NOM I TELÈFON DELS CONDUCTORS
for nom, telefon, estat_reserva in resultats3:
    print(f"{nom} | {telefon} --- {estat_reserva}")

