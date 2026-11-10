# Nivell 3: Actualitzacions (UPDATE) complexes

# IMPORTEM EL MYSQL
import mysql.connector

# ENS CONNECTEM AMB LA BD I FEM EL CURSOR
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# Exercici 6: Escriu un script que demani a l'usuari la matrícula d'un
# vehicle i un nou quilometratge, i actualitzi la taula VEHICLES amb
# aquest valor nou. Comprova amb cursor.rowcount que s'hagi modificat
# correctament.

# DEMANEM LA MATRÍCULA I ELS NOUS KM I HO GUARDEM EN VARIABLES
matricula = input("Escriu la matrícula del vehicle que busques: ")
quilometratge = input("Escriu el quilometratge que li vols canviar al vehicle: ")

# FEM EL UPDATE A VEHICLES, CANVIANT EL QUILOMETRATGE DEL COTXE AMB LA
# MATRÍCULA GUARDADA. EXECUTEM I FEM EL COMMIT
sql = "UPDATE VEHICLES SET QUILOMETRATGE = %s WHERE MATRICULA = %s"
valors = (quilometratge, matricula)
cursor.execute(sql, valors)
connexio.commit()

# IMPRIMIM LES FILES MODIFICADES
print(f"Files modificades: {cursor.rowcount}")

# Exercici 7: Fes un script que actualitzi l'estat de totes les reserves
# que estiguin com a 'PENDENT' a passar a ser 'ACTIVA' d'un cop (recorda
# comprovar quantes files s'han afectat).

# FEM EL UPDATE EN RESERVES, CANVIEM TOTES LES RESERVES EN ESTAT 'PENDENT'
# PER ESTAT 'ACTIVA'. EXECUTEM I FEM EL COMMIT
sql = "UPDATE RESERVES SET ESTAT_RESERVA = %s WHERE ESTAT_RESERVA = %s"
valors = ("ACTIVA", "PENDENT")
cursor.execute(sql, valors)
connexio.commit()

# MOSTREM TOTES LES FILERES MODIFICADES
print(f"Files modificades: {cursor.rowcount}")


