# 5. Gestor de la llista de la compra interactiva

# Concepte: Llistes, .append(), .sort(), bucle while, input().

# Enunciat:
# Crea una llista buida anomenada compra.
# Fes un bucle while que demani a l'usuari un producte per afegir.
# Si l'usuari escriu la paraula "fi", el bucle s'ha d'aturar.
# Si no, afegeix el producte a la llista amb .append().
# Un cop acabat, ordena la llista alfabèticament amb .sort() i mostra-la
# per pantalla iterant-la amb un for o directament amb un f-string.

compra = []

producte = input("Afegeix productes a la llista de la compra. Escriu 'fi' quan hagis acabat: ").lower()

while producte != "fi":
    compra.append(producte)
    producte = input("Afegeix un altre producte o escriu 'fi': ").lower()

compra.sort()

print("Llista de la compra: ")
for produce in compra:
    print(produce)

print(f"Llista de la compra: {compra}")