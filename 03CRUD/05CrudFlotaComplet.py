# Nivell 5: El repte integrat (El CRUD complet en un sol script)

# Exercici 10 (El gran projecte): Construeix un petit script modular (o
# amb funcions a Python) que faci el següent cicle:

# Crea un nou registre de prova a la taula VEHICLES.
# Llegeix el vehicle acabat de crear per confirmar que existeix a la
# base de dades.
# Actualitza el seu estat a 'EN TALLER'.
# Esborra el vehicle de la base de dades per deixar-ho tot net.

# IMPORTEM EL MYSQL
import mysql.connector
# FEM LA CONNEXIÓ I EL CURSOR
connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# CREEM UNA VARIABLE PER GUARDAR L'ID DEL REGISTRE QUE AFEGIREM I TRACTAREM
id_nou = None

# CREEM LA FUNCIÓ PER AFEGIR EL NOU REGISTRE
def create_registre():
    # DECLAREM LA VARIABLE DE L'ID COM A GLOBAL DINS DE LA FUNCIÓ PER A QUE
    # PYTHON ENTENGUI QUE ÉS LA MATEIXA I NO UNA NOVA AMB EL MATEIX NOM
    global id_nou

    # DEMANEM LES DADES DEL NOU VEHICLE AL USUARI I HO GUARDEM TOT EN VARIABLES
    matricula = input("Escriu la matrícula del nou vehicle: ")
    marca = input("Escriu la marca: ")
    model = input("Escriu el model del vehicle: ")
    estat = input("Escriu en quin estat es troba: ")
    quilometratge = input("Escriu el quilometratge que te: ")

    # FEM LA CONSULTA SQL: UN INSERT INTO EN VEHICLES AMB LES DADES QUE LI
    # HAVÍEM DEMANAT A L'USUARI. EXECUTEM I FEM EL COMMIT
    sql = "INSERT INTO VEHICLES (MATRICULA, MARCA, MODEL, ESTAT, QUILOMETRATGE) VALUES (%s, %s, %s, %s, %s)"
    valors = (matricula, marca, model, estat, quilometratge)
    cursor.execute(sql, valors)
    connexio.commit()

    # MOSTREM QUE S'HA GENERAT UN NOU VEHICLE_ID I EL GUARDEM EN LA VARIABLE
    # QUE HAVÍEM FET AL PRINCIPI PER A L'ID
    print(f"S'ha afegit el nou registre correctament. ID generat: {cursor.lastrowid}")
    id_nou = cursor.lastrowid

# FEM LA FUNCIÓ PER LLEGIR LA BD I MOSTRAR EL REGISTRE QUE ACABEM D'AFEGIR
def read_registre():
    # FEM UNA CONSULTA SQL PER MOSTRAR UN VEHICLE, ON EL VEHICLE_ID ÉS L'ÚLTIM
    # ID GENERAT EN L'ANTERIOR FUNCIÓ. HO EXECUTEM I FEM UN FETCHALL QUE
    # GUARDEM EN LA VARIABLE RESULTATS
    sql = ("SELECT MATRICULA, MARCA, MODEL, ESTAT, QUILOMETRATGE FROM VEHICLES WHERE VEHICLE_ID = %s")
    valor = (id_nou,)
    cursor.execute(sql, valor)
    resultats = cursor.fetchall()

    # AMB UN FOR MOSTREM ELS RESULTATS DE MANERA MÉS ESTÈTICA
    print("--- VEHICLE AFEGIT ---")
    for matricula, marca, model, estat, quilometratge in resultats:
        print(f"Vehicle: {matricula} - {marca} {model} - {estat} - {quilometratge}km")

# FEM LA FUNCIÓ PER ACTUALITZAR L'ESTAT A 'EN TALLER'
def update_registre():
    # FEM LA CONSULTA SQL PER ACTUALITZAR EL REGISTRE QUE TINGUI L'ID GUARDAT
    sql = "UPDATE VEHICLES SET ESTAT = %s WHERE VEHICLE_ID = %s"
    valors = ("EN TALLER", id_nou)
    cursor.execute(sql, valors)
    connexio.commit()

    # MOSTREM LES FILERES QUE S'HAN ACTUALITZAT
    print(f"Files actualitzades correctament: {cursor.rowcount}")

# FEM LA FUNCIÓ PER ELIMINAR EL REGISTRE EN QÜESTIÓ
def delete_registre():
    # LA CONSULTA SQL QUE ELIMINA EL VEHICLE AMB L'ID QUE TENIM GUARDADA
    sql = "DELETE FROM VEHICLES WHERE VEHICLE_ID = %s"
    valor = (id_nou,)
    cursor.execute(sql, valor)
    connexio.commit()

    print(f"S'han esborrat {cursor.rowcount} registres correctament")

# CRIDEM TOTES LES FUNCIONS
create_registre()
read_registre()
update_registre()
delete_registre()
# HO TANQUEM TOT
cursor.close()
connexio.close()



