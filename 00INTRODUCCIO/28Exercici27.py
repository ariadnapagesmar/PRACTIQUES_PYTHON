# 7. Sistema de reserves de teatre (Diccionaris niats / Estructures complexes)

# Crea un programa de gestió de seients d'un teatre petit representat per un
# diccionari on les claus són els números de fila (del 1 al 3) i els valors són
# llistes de 4 elements que indiquen si estan lliures ("Lliure") o ocupats ("Ocupat").
# Permet a l'usuari triar fila i seient per reservar-lo, comprovant abans si ja
# estava ocupat.

# CREEM EL DICCIONARI DE TRES FILERES I 4 SEIENTS, INDICANT SI ESTAN LLIURES O OCUPATS
teatre = {
    1: ["Lliure", "Ocupat", "Lliure", "Ocupat"],
    2: ["Ocupat", "Lliure", "Lliure", "Lliure"],
    3: ["Lliure", "Ocupat", "Ocupat", "Lliure"],
}

# DECLAREM LES VARIABLES PERÒ LI ASSIGNEM VALOR 0 DE MOMENT
fila = 0
seient = 0

# UN BUCLE QUE DEMANI LA FILA A L'USUARI FINS QUE SIGUI ENTRE 1 I 3
while fila > 3 or fila < 1:
    fila = int(input("Escull una filera del teatre per reservar un seient (del 1 al 3): "))
    if fila > 3 or fila < 1:
        print("Número de filera invàlid.")

# UN ALTRE BUCLE QUE DEMANI EL SEIENT FINS QUE SIGUI ENTRE 1 I 4
while seient > 4 or seient < 1:
    seient = int(input("Escull el seient (del 1 al 4): "))
    if fila > 4 or fila < 1:
        print("Número de seient invàlid.")

# QUAN TINGUEM TANT LA FILERA COM EL SEIENT QUE VOL RESERVAR L'USUARI, COMPROVEM SI
# ESTÀ LLIURE O OCUPAT. EL RESERVEM SI ESTÀ LLIURE, O AVISEM SI ESTÀ OCUPAT.
if teatre[fila][seient - 1] == "Lliure":
    print(f"Seient reservat --- fila: {fila}, seient: {seient}")
    teatre[fila][seient - 1] = "Ocupat"
    for fila, seient in teatre.items():
        print(f"{fila}: {seient}")
elif teatre[fila][seient - 1] == "Ocupat":
    print(f"El seient {seient} de la filera {fila} ja està ocupat. Escull un altre.")