# 3. Gestor de notes d'alumnes amb Tuples i Llistes

# Crea una llista que contingui diverses tuples amb informació d'alumnes:
# [("Anna", 7.5, 8.0), ("Marc", 4.0, 5.5), ...]. Utilitza un bucle for
# (o desempaquetat de tuples) per calcular la nota mitjana de cadascun.
# Fes servir una llista per comprensió per filtrar i crear una nova llista
# només amb els alumnes que hagin aprovat (mitjana >= 5)

# CREEM UNA LLISTA AMB TUPLES ON FICA EL NOM I LES NOTES DE L'ALUMNE
alumnes = [
    ("Anna", 7.5, 8.0),
    ("Marc", 4.0, 5.5),
    ("Júlia", 9.0, 9.5),
    ("Pau", 3.5, 4.0),
    ("Clàudia", 6.0, 6.5),
    ("Joan", 5.0, 4.5)
]

# CREEM LA NOVA LLISTA AMB LES MITJANES DE TOTS ELS ALUMNES, PRIMER BUIDA
mitjana_alumnes = []

# EN EL BUCLE OMPLIM AQUESTA NOVA LLISTA, FENT EL CÀLCUL DE LA MITJANA DE CADASCÚN
for nom, nota1, nota2 in alumnes:
    nota_mitjana = (nota1 + nota2) / 2
    mitjana_alumnes.append((nom, nota_mitjana))

print(mitjana_alumnes)

# CREEM UNA NOVA LLISTA, AQUEST COP PER COMPRENSIÓ, ON NOMÉS GUARDAREM EL NOM I LA
# MITJA DELS ALUMNES QUE HAGIN APROVAT (>= 5)
alumnes_aprovats = [(nom, nota) for nom, nota in mitjana_alumnes if nota >= 5]

# I MOSTREM L'ÚLTIMA LLISTA AMB ELS ALUMNES APROVATS I LES SEVES MITJANES
for alumne in alumnes_aprovats:
    print(f"{alumne[0]} --- {alumne[1]}")

