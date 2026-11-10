# Nivell 4: Esborrats segurs (DELETE)

import mysql.connector

connexio = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_bd"
)
cursor = connexio.cursor()

# Exercici 8: Escriu un script que demani un MANTENIMENT_ID per teclat i
# l'elimini de la base de dades de manera segura, mostrant un missatge
# de confirmació si s'ha esborrat o un avís si l'ID no existia.




# Exercici 9: Fes un script que netegi la base de dades esborrant totes
# aquelles reserves que hagin quedat amb l'estat 'FINALITZADA'.




