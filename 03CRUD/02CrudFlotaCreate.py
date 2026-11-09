# Nivell 2: Insercions de dades (CREATE)

# Exercici 4: Escriu un bloc de codi en Python que insereixi un nou vehicle
# a la taula VEHICLES fent servir marcadors %s (per exemple:
# matrícula '7777ZZZ', marca 'Renault', model 'Clio', estat 'DISPONIBLE',
# quilometratge 15000). Recorda fer el connexio.commit()!

# IMPORTEM EL CONNECTOR MYSQL
import mysql.connector

# OBRIM CONNEXIÓ AMB LA BD
connexio1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
# CREEM EL CURSOR
cursor1 = connexio1.cursor()

# FEM L'INSERT INTO DINS D'UNA VARIABLE, PERÒ NO ESCRIVIM ELS VALORS ENCARA
sql = "INSERT INTO VEHICLES (MATRICULA, MARCA, MODEL, ESTAT, QUILOMETRATGE) VALUES (%s, %s, %s, %s, %s)"
# ESCRIVIM ELS VALORS EN UN ALTRE VARIABLE DIFERENT
valors = ("0000AAA", "Hyundai", "Tucson", "OCUPAT", 5500)
# EXECUTEM LA COMANDA, LA VARIABLE AMB L'INSERT INTO + LA VARIABLE AMB ELS VALORS
cursor1.execute(sql, valors)

# FEM EL COMMIT PER A QUE GUARDI LES DADES
connexio1.commit()
# DIEM PER CONSOLA LA NOVA FILA QUE S'HA GENERAT EN VEHICLES
print(f"S'ha inserit el vehicle correctament. ID generat: {cursor1.lastrowid}")
# HO TANQUEM TOT
cursor1.close()
connexio1.close()

# Exercici 5: Fes un script que demani a l'usuari per teclat (input()) el
# nom, el carnet i el telèfon d'un nou conductor, i l'insereixi
# automàticament a la taula CONDUCTOR.

# GUARDEM EN VARIABLES LES RESPOSTES QUE ESCRIGUI L'USUARI PER CONSOLA
print("BENVINGUT A LA FLOTA DELS NOSTRES VEHICLES")
nom = input("Escriu el nom del nou conductor: ").title()
carnet = input("Escriu el carnet de conduir del usuari: ").upper()
telefon = input("Escriu el número de telèfon del conductor: ")

# CREEM LA CONNEXIÓ I EL CURSOR
connexio2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor2 = connexio2.cursor()

# FEM LA CONSULTA AMB L'INSERT INTO EN UNA VARIABLE
sql = "INSERT INTO CONDUCTORS (NOM, CARNET, TELEFON) VALUES (%s, %s, %s)"
# I LES RESPOSTES DE L'USUARI EN UN ALTRE VARIABLE
valors = (nom, carnet, telefon)
# EXECUTEM LA COMANDA AMB LES DUES VARIABLES
cursor2.execute(sql, valors)
# FEM EL COMMIT
connexio2.commit()

# MOSTREM LA NOVA FILA QUE S'HA GENERAT EN CONDUCTORS
print(f"S'ha afegir el nou conductor correctament. ID generat: {cursor2.lastrowid}")
# HO TANQUEM TOT
cursor2.close()
connexio2.close()