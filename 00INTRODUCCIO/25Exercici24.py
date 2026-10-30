# 4. Joc de taula d'intersecció de gustos (Conjunts / Sets + Input)

# Crea dos conjunts fixos de gèneres de pel·lícules preferits de dues persones
# diferents (per exemple, persona1 = {"terror", "comèdia", "ciència-ficció"}).
# Demana a l'usuari que introdueixi un nou gènere a través de l'input().
# Afegeix-lo al conjunt de la persona1 (fent servir .add()). Després, calcula
# i mostra per pantalla:

# Els gustos que comparteixen ambdós (intersecció).
# Tots els gèneres únics combinats (unió).
# Els gustos exclusius de la persona 1 (diferència).

# CREEM DUES PERSONES (DOS CONJUNTS) AMB ELS GÈNERES DE PELIS QUE ELS AGRADA
persona1 = {"terror", "comèdia", "ciència-ficció"}
persona2 = {"romanç", "misteri", "comèdia"}

# DEMANEM A L'USUARI QUE AFEGEIXI UN NOU GÈNERE A PERSONA1
nou_genere = input("Escriu un nou gènere de pel·lícules: ")

# L'AFEGIM AL CONJUNT
persona1.add(nou_genere)

# MOSTREM ELS GÈNERES QUE TENEN LES DUES PERSONES EN COMÚ
en_comu = persona1 & persona2
print(f"Gustos en comú: {en_comu}")

# MOSTREM TOTS ELS GÈNERES DIFERENTS QUE HI HA EN ELS DOS CONJUNTS
generes_tots = persona1 | persona2
print(f"Tots els gèneres: {generes_tots}")

# MOSTREM ELS GÈNERES QUE NOMÉS TÉ PERSONA1
unic_persona1 = persona1 - persona2
print(f"Gustos exclusius de persona1: {unic_persona1}")