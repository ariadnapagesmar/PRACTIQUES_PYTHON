# 2. Analitzador de freqüència de paraules (Strings + Diccionaris)

# Demanar a l'usuari que introdueixi una frase llarga. Utilitza mètodes de string
# (com .lower() i .split()) per separar totes les paraules. Després, utilitza un
# bucle per crear un diccionari on la clau sigui cada paraula i el valor sigui el
# nombre de vegades que apareix repetida a la frase. Imprimeix el diccionari
# resultant de manera ordenada o neta.

# FRASE EXEMPLE: Aquest curs de python és molt interessant i aprendre python m'està agradant moltíssim perquè programar és divertit

frase = input("Escriu una frase llarga: ").lower().split()

print(frase)

diccionari_frase = {}

for paraula in frase:
    diccionari_frase[paraula] = frase.count(paraula)
    print(f"{paraula} -- {diccionari_frase[paraula]}")


