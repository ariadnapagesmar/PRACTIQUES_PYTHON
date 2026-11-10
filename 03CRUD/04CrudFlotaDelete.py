# Nivell 4: Eliminacions (DELETE)

# Exercici 8: Escriu un script que elimini un manteniment concret de la taula
# MANTENIMENTS a partir del seu MANTENIMENT_ID.

import mysql.connector

connexio1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor1 = connexio1.cursor()

sql = "DELETE FROM MANTENIMENTS WHERE MANTENIMENT_ID = %s"
valor = (1,)

cursor1.execute(sql, valor)
connexio1.commit()

print(f"S'han esborrat {cursor1.rowcount} registres.")

cursor1.close()
connexio1.close()

# Exercici 9: Fes una lògica que esborri totes aquelles reserves que tinguin
# l'estat 'CANCEL·LADA' o 'FINALITZADA' (recorda sempre validar amb un
# WHERE per no esborrar tota la taula sense voler!).

connexio2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestor_flota_db"
)
cursor2 = connexio2.cursor()

sql = "DELETE FROM RESERVES WHERE ESTAT_RESERVA = %s"
valor = ("FINALITZADA",)

cursor2.execute(sql, valor)
connexio2.commit()

print(f"S'han esborrat {cursor2.rowcount} registres.")

cursor2.close()
connexio2.close()


