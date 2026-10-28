# 8. Comptador de paraules úniques (Conjunts / Sets)

# Concepte: Set, conversió de llistes a sets, operacions de conjunts.

# Enunciat: Tens una llista de colors on alguns es repeteixen:
# colors = ["vermell", "blau", "verd", "vermell", "groc", "blau", "vermell"].

# Converteix aquesta llista en un conjunt (set) per eliminar automàticament els duplicats.

# Demana a l'usuari per input() un color qualsevol.

# Comprova si aquest color es troba dins del conjunt de colors únics
# i mostra un missatge adaptat amb un f-string.

colors = ["vermell", "blau", "verd", "vermell", "groc", "blau", "vermell"]

conjunt_colors = set(colors)

resposta = input("Escull un color: ").lower()

if resposta in conjunt_colors:
    print(f"El color {resposta} SÍ es troba dins del conjunt de colors únics.")
else:
    print(f"El color {resposta} NO es troba dins de la llista de colors únics.")