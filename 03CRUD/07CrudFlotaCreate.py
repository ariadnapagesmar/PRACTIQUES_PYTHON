# Nivell 2: Insercions (CREATE) amb relacions (Foreign Keys)

# IMPORTEM EL MYSQL
import mysql.connector

# CONNECTEM LA BD I CREEM EL CURSOR
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# Exercici 4: Escriu un script en Python que insereixi un nou conductor
# amb dades inventades a la taula CONDUCTOR i mostri per pantalla el seu
# nou ID generat automàticament (cursor.lastrowid).

# DEMANEM LES DADES DEL CONDUCTOR I LES GUARDEM EN VARIABLES
nom = input("Escriu el nom del nou conductor: ")
carnet = input("Escriu el carnet del nou conductor: ")
telefon = input("Escriu el telèfon del nou conductor: ")

# FEM L'INSERT INTO EN LA TAULA CONDUCTORS AMB LES DADES DE L'USUARI
sql = "INSERT INTO CONDUCTORS (NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
valors = (nom, carnet, telefon)
# EXECUTEM LA COMANDA I FEM EL COMMIT
cursor.execute(sql, valors)
connexio.commit()

# MOSTREM L'ID DEL NOU CONDUCTOR
print(f"Conductor registrat: ID {cursor.lastrowid} - {nom} - {carnet} - {telefon}")

# Exercici 5: Fes un script que registri un nou manteniment per a un
# vehicle existent. Haurà de demanar per teclat l'ID del vehicle, la
# descripció i el cost, i inserir-ho a la taula MANTENIMENTS.

# DEMANEM LES DADES SOBRE EL MANTENIMENT QUE AFEGIREM I HO GUARDEM EN VARIABLES
id_vehicle = input("Escriu l'ID del vehicle que anirà a manteniments: ")
descripcio= input("Descriu el problema del vehicle: ")
cost = input("Escriu el cost total del manteniment: ")
data_manteniment = input("Escriu la data en format any-mes-dia: ")

# FEM L'INSERT INTO EN LA TAULA MANTENIMENTS AMB LES DADES DE L'USUARI
sql = "INSERT INTO MANTENIMENTS (VEHICLE_ID, DESCRIPCIO, COST, DATA_MANTENIMENT) VALUES (%s, %s, %s, %s)"
valors = (id_vehicle, descripcio, cost, data_manteniment)
# EXECUTEM LA COMANDA I FEM EL COMMIT
cursor.execute(sql, valors)
connexio.commit()

# MOSTREM L'ID DEL NOU MANTENIMENT
print(f"Manteniment registrat: ID {cursor.lastrowid} - {id_vehicle} - {descripcio} - {cost}")

# HO TANQUEM TOT
cursor.close()
connexio.close()