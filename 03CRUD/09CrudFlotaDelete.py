# Nivell 4: Esborrats segurs (DELETE)

# IMPORTEM EL MYSQL I FEM EL CURSOR
import mysql.connector

connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor = connexio.cursor()

# Exercici 8: Escriu un script que demani un MANTENIMENT_ID per teclat i
# l'elimini de la base de dades de manera segura, mostrant un missatge
# de confirmació si s'ha esborrat o un avís si l'ID no existia.

# PREGUNTEM A L'USUARI QUIN ID DE MANTENIMENT VOL ELIMINAR
id_manteniment = int(input("Escriu l'ID del manteniment que vols eliminar: "))

# FEM LA COMANDA DELETE PER ELIMINAR EL REGISTRE DE MANTENIMENT AMB L'ID
# DE L'USUARI. EXECUTEM LA COMANDA I FEL EL COMMIT
sql = "DELETE FROM MANTENIMENTS WHERE MANTENIMENT_ID = %s"
valor = (id_manteniment,)
cursor.execute(sql, valor)
connexio.commit()

# SI S'HA MODIFICAT ALGUNA FILERA, DIEM QUE S'HA ELIMINAT CORRECTAMENT
# SI NO, AVISEM QUE AQUEST ID NO EXISTEIX.
if cursor.rowcount > 0:
    print(f"El manteniment amb ID {id_manteniment} ha sigut eliminat correctament.")
else:
    print(f"No hi ha cap manteniment amb ID {id_manteniment}.")

# Exercici 9: Fes un script que netegi la base de dades esborrant totes
# aquelles reserves que hagin quedat amb l'estat 'FINALITZADA'.

# FEM LA COMANDA DIRECTAMENT I ELIMINEM TOTES LES RESERVES QUE TINGUIN
# L'ESTAT 'FINALITZADA'
sql = "DELETE FROM RESERVES WHERE ESTAT_RESERVA = %s"
valor = ("FINALITZADA",)
cursor.execute(sql, valor)
connexio.commit()

print(f"S'han eliminat {cursor.rowcount} fileres correctament.")


