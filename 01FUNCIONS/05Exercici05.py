# 5. Filtrar notes amb llista per comprensió dins d'una funció (Mitjà)

# Escriu una funció anomenada filtra_aprovats(diccionari_notes) que rebi un
# diccionari on les claus són noms d'alumnes i els valors són les seves notes
# (p.ex., {"Anna": 8.5, "Marc": 4.2, "Pau": 6.0}). La funció ha de retornar una
# nova llista només amb els noms dels alumnes suspesos (nota < 5) utilitzant
# una llista per comprensió a l'interior.

# CREEM UN DICCIONARI AMB EL NOM DELS ALUMNES COM A CLAU I LA NOTA COM A VALOR
notes_alumnes = {
    "Ariadna": 8.5,
    "Marc": 4.2,
    "Júlia": 9.0,
    "Pau": 3.8,
    "Laura": 5.0,
    "Carles": 2.1,
    "Marta": 7.5,
    "Joan": 4.9
}

# CREEM UNA FUNCIÓ QUE RETORNI UNA NOVA LLISTA PER COMPRENSIÓ QUE FILTRI I GUARDI
# NOMÉS ELS NOMS DELS ALUMNES QUE HAGIN TRET MENYS DE 5, PERÒ NO CREEM LA NOVA LLISTA
# ENCARA, SINO QUE FIQUEM EL CODI EN EL RETURN
def filtra_aprovats(diccionari_alumnes):
    return [nom for nom, nota in diccionari_alumnes.items() if nota < 5]

# ARA, FORA DE LA FUNCIÓ, CREEM LA NOVA LLISTA I DINS CRIDEM LA FUNCIÓ
alumnes_suspesos = filtra_aprovats(notes_alumnes)

# FEM UN BUCLE QUE MOSTRI TOTS ELS NOMS DE LA NOVA LLISTA, I PER TROBAR LA SEVA
# NOTA LA BUSQUEM EN L'ANTERIOR LLISTA BUSCANT-LA AMB EL NOM DE L'ALUMNE
for alumne in alumnes_suspesos:
    nota = notes_alumnes[alumne]
    print(f"{alumne} --- {nota}")