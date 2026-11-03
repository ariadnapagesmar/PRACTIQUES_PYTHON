# 1. Control d'inventari persistent amb fitxers (open + try-except)

# Agafa el teu codi de la botiga i adapta'l perquè llegeixi l'estoc inicial d'un
# fitxer de text (inventari.txt) en arrencar el programa. Si el fitxer no existeix,
# utilitza un bloc try-except per capturar l'excepció FileNotFoundError, crear el
# fitxer automàticament amb l'estoc per defecte, i fer que en seleccionar "Sortir",
# el programa guardi i actualitzi automàticament tot l'estoc actual al fitxer abans
# de tancar-se.

# 1. Funció per carregar l'inventari
def carregar_fitxer(nom_fitxer):
    diccionari_estoc = {}
    try:
        with open(nom_fitxer, "r") as arxiu:
            for linia in arxiu:
                linia = linia.strip()
                if linia:
                    producte, quantitat = linia.split(":")
                    diccionari_estoc[producte] = int(quantitat)
        print("S'ha carregat l'inventari correctament des del fitxer.")
    except FileNotFoundError:
        print("No hem trobat cap fitxer previ. El crearem des de zero...")
        diccionari_estoc = {"pomes": 10, "llet": 5, "pa": 3, "ous": 24, "patates": 14}
        actualitzar_fitxer(nom_fitxer, diccionari_estoc)

    return diccionari_estoc


# 2. Funció per actualitzar/guardar el fitxer
def actualitzar_fitxer(nom_fitxer, diccionari):
    try:
        with open(nom_fitxer, "w") as arxiu:
            for producte, quantitat in diccionari.items():
                arxiu.write(f"{producte}:{quantitat}\n")
        print("L'inventari a l'arxiu ha sigut actualitzat amb èxit.")
    except Exception as e:
        print(f"Hi ha hagut un error a l'hora d'escriure al fitxer: {e}")


def mostrar_estoc(diccionari):
    print("\nEls nostres productes: ")
    for producte, estoc in diccionari.items():
        print(f"{producte} --- {estoc}")


def comprar_producte(diccionari, producte, quantitat):
    if producte in diccionari.keys():
        if quantitat <= diccionari[producte]:
            diccionari[producte] -= quantitat
            print(f"Producte comprat amb èxit!\n{producte} --- {quantitat}")
        else:
            print(f"No tenim l'estoc suficient de: {producte}")
    else:
        print("Aquest producte no és vàlid.")


def ampliar_estoc(diccionari, producte, quantitat):
    if producte in diccionari.keys():
        diccionari[producte] += quantitat
        print(f"Producte afegit amb èxit!\n{producte} --- {quantitat}")
    else:
        print("Aquest producte no és vàlid.")


# --- FLUX PRINCIPAL ---
FITXER_INVENTARI = "inventari.txt"
diccionari_estoc = carregar_fitxer(FITXER_INVENTARI)

accio_usuari = ""

while accio_usuari != "4":
    accio_usuari = input("\nBenvingut a la nostra botiga online.\n"
                         "Seleccioni què vol fer escrivint el número de l'acció.\n"
                         "1. Consultar estoc.\n"
                         "2. Comprar producte.\n"
                         "3. Ampliar estoc.\n"
                         "4. Sortir (i actualitzar el fitxer).\n"
                         "Opció: ")
    if accio_usuari == "1":
        mostrar_estoc(diccionari_estoc)

    elif accio_usuari == "2":
        producte = input("Quin producte vol comprar? ").lower()
        if producte in diccionari_estoc.keys():
            try:
                # CONVERTIM A INT EL QUE RETORNA L'INPUT
                quantitat = int(input("Quina quantitat vol comprar? "))
                if quantitat > 0:
                    comprar_producte(diccionari_estoc, producte, quantitat)
                else:
                    print("La quantitat ha de ser major a 0.")
            except ValueError:
                print("Error: has d'introduir un valor enter vàlid.")
        else:
            print("Aquest producte no existeix.")

    elif accio_usuari == "3":
        producte = input("De quin producte vol ampliar estoc? ").lower()
        if producte in diccionari_estoc.keys():
            try:
                # CONVERTIM A INT EL QUE RETORNA L'INPUT
                quantitat = int(input("Quina quantitat vol afegir? "))
                if quantitat > 0:
                    ampliar_estoc(diccionari_estoc, producte, quantitat)
                else:
                    print("La quantitat ha de ser major a 0.")
            except ValueError:
                print("Error: has d'introduir un valor enter vàlid.")
        else:
            print("Aquest producte no existeix.")

    elif accio_usuari == "4":
        actualitzar_fitxer(FITXER_INVENTARI, diccionari_estoc)
        print("Fins a la propera!")

    else:
        print("Acció no vàlida.")