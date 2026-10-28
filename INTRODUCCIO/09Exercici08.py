# 8. Gestió d'un diccionari

# Concepte: Diccionaris, mètodes .keys(), .values(), .update().

# Enunciat:
# Crea un diccionari anomenat pelicula amb les claus "titol", "director"
# i "any" (posa-li valors inventats).
# Afegeix una nova clau "genere" utilitzant el mètode .update().
# Imprimeix només les claus del diccionari i després només els valors
# per separat emprant els mètodes corresponents de l'apunt.

pelicula = {
    "titol": "Pinocho",
    "director": "Guillermo del Toro",
    "any": 2023
}

pelicula.update({"genere": "Dibuixos animats"})

print(pelicula.keys())
print(pelicula.values())