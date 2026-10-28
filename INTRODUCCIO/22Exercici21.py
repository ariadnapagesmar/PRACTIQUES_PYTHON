# 1. Control d'inventari d'una botiga (Diccionaris + Input)

# Crea un programa que comenci amb un diccionari de productes i estocs
# (per exemple: {"pomes": 10, "llet": 5, "pa": 2}). Fes un bucle while que
# permeti a l'usuari triar entre "comprar" (restar unitats del producte si
# n'hi ha prou) o "ampliar" (afegir més stock). Si l'usuari escriu "sortir",
# el programa s'atura i mostra l'inventari final actualitzat.

# CREEM UN DICCIONARI AMB ELS PRODUCTES I EL SEU ESTOC
estoc_productes = {"pomes": 10, "llet": 5, "pa": 3, "ous": 24, "patates": 14}

# MOSTREM L'ESTOC PER LA CONSOLA
print("Benvingut a la nostra botiga online. Aquests són els productes que tenim en estoc: ")
for producte, stock in estoc_productes.items():
    print(f"{producte}: {stock}")

# PREGUNTEM A L'USUARI QUÈ VOL FER I SI NO RESPON BÉ HO REPETIM FINS QUE DIGUI 'COMPRAR',
# 'AMPLIAR' O 'SORTIR'
resposta = input("Vols comprar algo o ampliar l'estoc? Escriu 'comprar' o 'ampliar'. "
                 "O escriu 'sortir' si ja has acabat: ").lower()
while resposta != "comprar" and resposta != "ampliar" and resposta != "sortir":
    resposta = input("Acció NO vàlida. Escriu 'comprar', 'ampliar' o 'sortir': ")

# ENTREM EN UN BUCLE QUE NOMÉS S'ATURA SI L'USUARI ESCRIU 'SORTIR'
while resposta != "sortir" and (resposta == "comprar" or resposta == "ampliar"):
    if resposta == "comprar":
        resposta_producte = input("Quin producte vols comprar? ").lower()
        if resposta_producte in estoc_productes:
            resposta_estoc = int(input(f"Quina quantitat vols comprar de {resposta_producte}? "))
            if estoc_productes[resposta_producte] >= resposta_estoc > 0:
                estoc_productes[resposta_producte] -= resposta_estoc
                print(f"Compra realitzada: {resposta_producte} - {estoc_productes[resposta_producte]}")
            else:
                print("Quantitat no vàlida.")
        else:
            print("Aquest producte no el tenim.")

        resposta = input("Continues en la botiga online. Escriu 'comprar', "
                         "'ampliar' o 'sortir': ").lower()
        while resposta != "comprar" and resposta != "ampliar" and resposta != "sortir":
            resposta = input("Acció NO vàlida. Escriu 'comprar', 'ampliar' o 'sortir': ")

    elif resposta == "ampliar":
        resposta_producte = input("De quin producte vols afegir estoc? ").lower()
        if resposta_producte in estoc_productes:
            resposta_estoc = int(input(f"Quina quantitat de {resposta_producte} vols afegir? "))
            if resposta_estoc > 0:
                estoc_productes[resposta_producte] += resposta_estoc
                print(f"Estoc actualitzat: {resposta_producte} - {estoc_productes[resposta_producte]}")
            else:
                print("Quantitat NO vàlida.")
        else:
            print("Producte invàlid.")

        resposta = input("Continues en la botiga online. Escriu 'comprar', "
                         "'ampliar' o 'sortir': ").lower()
        while resposta != "comprar" and resposta != "ampliar" and resposta != "sortir":
            resposta = input("Acció NO vàlida. Escriu 'comprar', 'ampliar' o 'sortir': ")

for producte, stock in estoc_productes.items():
    print(f"{producte}: {stock}")