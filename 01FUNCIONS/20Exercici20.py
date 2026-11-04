# 10. La llista de la compra amb fitxer (Avançat petit)

# Crea un programa amb un petit menú de dues opcions:
# 1. Afegir producte: Demana un producte per input() i l'afegeix al final d'un
# fitxer compra.txt (usant el mode "a").
# 2. Veure la llista: Obre el fitxer en mode "r" i mostra tots els productes
# guardats fins al moment (protegint-ho amb un try-except per si el fitxer
# encara no s'ha creat).


def afegir_producte(producte):
    with open("compra.txt", "a") as arxiu:
        arxiu.write(f"\n{producte}")
        print("Producte afegit amb èxit.")

def veure_llista():
    try:
        with open("compra.txt", "r") as arxiu:
            print("Llista de la compra: ")
            contingut = arxiu.read()
            print(contingut)
    except FileNotFoundError:
        print("No existeix cap llista encara. Afegeix un producte primer.")

accio_usuari = ""

while accio_usuari != "3":
    accio_usuari= input("Escull l'acció que vols fer:\n"
          "1. Afegir un producte a la llista\n"
          "2. Veure els productes de la llista\n"
          "3. Sortir\n")
    if accio_usuari == "1":
        producte = input("Quin producte vols afegir? ").capitalize()
        afegir_producte(producte)
    elif accio_usuari == "2":
        veure_llista()
    elif accio_usuari == "3":
        print("Sortint...")
    else:
        print("Acció no vàlida.")