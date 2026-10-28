# 7. Modificar llistes amb mètodes

# Concepte: Mètodes de llistes (append, insert, remove, sort).

# Enunciat:

# Crea una llista buida anomenada dies.
# Afegeix "Dimecres" i "Dilluns" utilitzant .append().
# Insereix "Dimarts" a la posició correcta utilitzant .insert().
# Ordena la llista alfabèticament amb .sort() i imprimeix-la.

dies = []

dies.append("Dilluns")
dies.append("Dimecres")

dies.insert(1, "Dimarts")

dies.sort()

print(dies)

for dia in dies:
    print(dia)