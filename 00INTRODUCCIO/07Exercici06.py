# 6. Filtrar amb continue

# Concepte: range(), continue, operadors aritmètics (%).

# Enunciat: Fes un bucle for utilitzant range(10) (del 0 al 9).
# Fes servir continue perquè no s'imprimeixin els nombres parells,
# només els senars (pista: pots mirar si el residu de dividir entre 2
# és diferent de 0, o basar-te en el teu exemple de l'apunt).

for i in range(10):
    if i % 2 != 0:
        print(i)