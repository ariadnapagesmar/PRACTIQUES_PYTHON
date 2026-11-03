# 10. Gestor d'inventari modular de botiga (Expert / Màster)

# Agafa el teu codi de l'exercici 1 de la botiga (el que acabem de validar amb un 10!)
# i reestructura'l sencer utilitzant funcions per separar responsabilitats:

# Una funció mostrar_estoc(diccionari) que imprimeixi l'estoc actual.
# Una funció comprar_producte(diccionari, producte, quantitat) que gestioni les
# restes i retorni si s'ha pogut fer o no.
# Una funció ampliar_estoc(diccionari, producte, quantitat) que sumi les unitats.

# El flux principal del programa (while amb input) només s'ha de dedicar a demanar
# dades a l'usuari i cridar aquestes funcions.

# CREEM EL DICCIONARI AMB ELS PRODUCTES I EL SEU ESTOC
estoc_productes = {"pomes": 10, "llet": 5, "pa": 3, "ous": 24, "patates": 14}

# CREEM LA FUNCIÓ QUE MOSTRA TOTS ELS SEUS PRODUCTES I L'ESTOC DE MANERA BONICA
def mostrar_estoc(diccionari):
    print("Els nostres productes: ")
    for producte, estoc in diccionari.items():
        print(f"{producte} --- {estoc}")

# CREEM LA FUNCIÓ PER COMPRAR UN PRODUCTE
def comprar_producte(diccionari, producte, quantitat):
    # COMPROVEM QUE EL PRODUCTE EXISTEIX EN EL DICCIONARI
    if producte in diccionari.keys():
        # COMPROVEM QUE HI HA QUANTITAT SUFICIENT D'AQUEST PRODUCTE PER A L'USUARI
        if quantitat <= diccionari[producte]:
            diccionari[producte] -= quantitat
            print("Producte comprat amb éxit!\n"
                  f"{producte} --- {quantitat}")
        else:
            print(f"No tenim l'estoc suficient de: {producte}")
    else:
        print("Aquest producte no és vàlid.")

# CREEM LA FUNCIÓ QUE AFEGEIX ESTOC A UN PRODUCTE
def ampliar_estoc(diccionari, producte, quantitat):
    # COMPROVEM QUE EL PRODUCTE QUE HA ESCRIT L'USUARI EXISTEIX EN EL DICCIONARI
    # I AFEGIM L'ESTOC CORRESPONENT
    if producte in diccionari.keys():
        diccionari[producte] += quantitat
        print("Producte afegit amb éxit!\n"
              f"{producte} --- {quantitat}")
    else:
        print("Aquest producte no és vàlid.")

# PREGUNTEM A L'USUARI QUÈ VOL FER
accio_usuari = input("Benvingut a la nostra botiga online."
                     "Seleccioni què vol fer escrivint el número de l'acció.\n"
                      "1. Consultar estoc.\n"
                      "2. Comprar producte.\n"
                      "3. Ampliar estoc.\n"
                      "4. Sortir.\n")

# OBRIM UN BUCLE QUE NO PARI FINS QUE L'USUARI ESCRIGUI '4', QUE ÉS EL NÚMERO PER SORTIR
while accio_usuari != "4":
    # SI ESCULL '1', CRIDEM LA FUNCIÓ QUE MOSTRA L'ESTOC I TORNEM A PREGUNTAR PER L'ACCIÓ
    if accio_usuari == "1":
        mostrar_estoc(estoc_productes)
        accio_usuari = input("Seleccioni què vol fer escrivint el número de l'acció.\n"
                      "1. Consultar estoc.\n"
                      "2. Comprar producte.\n"
                      "3. Ampliar estoc.\n"
                      "4. Sortir.\n")
    # SI ESCRIU '2', PREGUNTEM QUIN PRODUCTE VOL COMPRAR I QUINA QUANTITAT ABANS DE
    # CRIDAR LA FUNCIÓ. DESPRÉS TORNEM A PREGUNTAR PER L'ACCIÓ
    elif accio_usuari == "2":
        producte = input("Quin producte vol comprar? ").lower()
        quantitat = int(input(f"Quina quantitat de {producte} vol comprar? "))
        comprar_producte(estoc_productes, producte, quantitat)
        accio_usuari = input("Seleccioni què vol fer escrivint el número de l'acció.\n"
                             "1. Consultar estoc.\n"
                             "2. Comprar producte.\n"
                             "3. Ampliar estoc.\n"
                             "4. Sortir.\n")
    # SI ESCRIU '3' FEM EXACTAMENT EL MATEIX QUE AMB EL '2'
    elif accio_usuari == "3":
        producte = input("De quin producte vol afegir estoc? ").lower()
        quantitat = int(input(f"Quina quantitat de {producte} vol afegir a l'estoc? "))
        ampliar_estoc(estoc_productes, producte, quantitat)
        accio_usuari = input("Seleccioni què vol fer escrivint el número de l'acció.\n"
                             "1. Consultar estoc.\n"
                             "2. Comprar producte.\n"
                             "3. Ampliar estoc.\n"
                             "4. Sortir.\n")
    # SI ESCRIU UN NÚMERO QUE NO SIGUI ENTRE L'1 I EL 4, AVISEM QUE L'ACCIÓ NO ÉS VÀLIDA
    # I TORNEM A PREGUNTAR
    else:
        print("Acció no vàlida.")
        accio_usuari = input("Seleccioni què vol fer escrivint el número de l'acció.\n"
                             "1. Consultar estoc.\n"
                             "2. Comprar producte.\n"
                             "3. Ampliar estoc.\n"
                             "4. Sortir.\n")