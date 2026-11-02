# 10. Gestor d'inventari modular de botiga (Expert / Màster)

# Agafa el teu codi de l'exercici 1 de la botiga (el que acabem de validar amb un 10!)
# i reestructura'l sencer utilitzant funcions per separar responsabilitats:

# Una funció mostrar_estoc(diccionari) que imprimeixi l'estoc actual.
# Una funció comprar_producte(diccionari, producte, quantitat) que gestioni les
# restes i retorni si s'ha pogut fer o no.
# Una funció ampliar_estoc(diccionari, producte, quantitat) que sumi les unitats.

# El flux principal del programa (while amb input) només s'ha de dedicar a demanar
# dades a l'usuari i cridar aquestes funcions.

estoc_productes = {"pomes": 10, "llet": 5, "pa": 3, "ous": 24, "patates": 14}

def mostrar_estoc(diccionari):
    for producte, estoc in diccionari.items():
        print(f"{producte} --- {estoc}")

mostrar_estoc(estoc_productes)

def ampliar_estoc(diccionari, producte, quantitat):
    if producte in diccionari.keys():
        estoc_productes[producte] += quantitat
        print(f"L'estoc del producte: '{producte}' ha estat actualitzat amb éxit.")
    else:
        print("Aquest producte no és vàlid.")