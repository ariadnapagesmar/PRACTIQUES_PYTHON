# Nivell 3: Actualitzacions (UPDATE)
from multiprocessing.forkserver import connect_to_new_process

# Exercici 6: Escriu un script que actualitzi el quilometratge d'un vehicle
# concret (per exemple, sumar-li o posar-li 25000 km a la matrícula '7777ZZZ')
# i comprovi quantes files s'han modificat amb cursor.rowcount.

# IMPORTEM EL MYSQL
import mysql.connector

# CONNECTEM LA BD I CREEM EL CURSOR
connexio1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor1 = connexio1.cursor()

# FEM LA CONSULTA SQL: SUMEM AL QUILOMETRATGE DE LA MATRÍCULA QUE LI PASSEM
sql = "UPDATE VEHICLES SET QUILOMETRATGE = QUILOMETRATGE + %s WHERE MATRICULA = %s"
valors = (1000, "0000AAA")

# EXECUTEM, FEM EL COMMIT I MOSTREM LES FILES QUE HAN CANVIAT
cursor1.execute(sql, valors)
connexio1.commit()
print(f"Files modificades: {cursor1.rowcount}")
# HO TANQUEM TOT
cursor1.close()
connexio1.close()

# Exercici 7: Fes una operació que canviï l'estat d'un vehicle dE 'OCUPAT'
# a 'DISPONIBLE' a partir de la seva matrícula.

# FEM LA CONNEXIÓ A LA BD I CREEM EL CURSOR
connexio2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor2 = connexio2.cursor()

# FEM LA CONSULTA SQL: CANVIEM L'ESTAT DEL VEHICLE AMB LA MATRÍCULA QUE LI PASSEM
sql = ("UPDATE VEHICLES SET ESTAT = %s WHERE MATRICULA = %s")
valors = ("OCUPAT", "0000AAA")

# EXECUTEM, FEM EL COMMIT I MOSTREM LES FILES MODIFICADES
cursor2.execute(sql, valors)
connexio2.commit()
print(f"Files modificades: {cursor2.rowcount}")
# HO TANQUEM TOT
cursor2.close()
connexio2.close()