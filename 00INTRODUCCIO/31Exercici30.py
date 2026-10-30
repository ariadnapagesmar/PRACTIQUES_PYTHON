# 10. Gestor de biblioteca amb préstecs i devolucions (Diccionaris + Tuples + While)

# Crea un diccionari de llibres on la clau és el títol del llibre i el valor és
# una tupla amb dos elements: (autor, exemplars_disponibles).
# Fes un bucle interactiu que permeti a l'usuari triar entre:

# "Prestec": Resta 1 exemplar si queden disponibles (si arriben a 0, avisa que no n'hi ha).
# "Retorn": Suma 1 exemplar al llibre corresponent.
# "Sortir": Mostra l'estat final de tota la biblioteca.

# CREEM LA BIBLIOTECA AMB LLIBRES, EL SEU AUTOR I EL SEU ESTOC
biblioteca = {
    "El quijote de la mancha": ("Miguel de Cervantes", 6),
    "1984": ("George Orwell", 4),
    "Cien años de soledad": ("Gabriel García Márquez", 5),
    "Crim i castig": ("Fiódor Dostoyevski", 3),
    "Orgull i prejudici": ("Jane Austen", 4),
    "La metamorfosi": ("Franz Kafka", 2),
    "El petit princep": ("Antoine de Saint-Exupéry", 7),
    "Hamlet": ("William Shakespeare", 3),
    "La divina comedia": ("Dante Alighieri", 2),
    "Moby dick": ("Herman Melville", 3)
}

# CREEM LA VARIABLE AMB L'ACCIÓ DE L'USUARI
resposta_accio = ""
print("Benvingut a la biblioteca.")

# OBRIM UN BUCLE QUE NOMÉS S'ATURI SI L'USUARI ESCRIU 'SORTIR'
while resposta_accio != "sortir":
    resposta_accio = input("Vols agafar un llibre (prestec), retornar un (retorn) "
                           "o sortir de la biblioteca (sortir)? ")
    # SI ESCRIU 'PRESTEC', LI PREGUNTEM QUIN LLIBRE VOL AGAFAR
    if resposta_accio == "prestec":
        llibre_prestec = input("Quin llibre vols emportar-te? ").capitalize()
        # SI EL LLIBRE ÉS CORRECTE, RESTEM AQUEST LLIBRE DE L'ESTOC (-1)
        if llibre_prestec in biblioteca.keys() and biblioteca[llibre_prestec][1] > 0:
            print(f"T'has emportat un exemplar de: {llibre_prestec}")
            autor = biblioteca[llibre_prestec][0]
            exemplars = biblioteca[llibre_prestec][1]
            biblioteca[llibre_prestec] = (autor, exemplars - 1)
        # SI EL NOM NO ÉS CORRECTE O NO TÉ ESTOC, AVISEM A L'USUARI
        else:
            print(f"Ho sentim molt, però no ens queden exemplars de: {llibre_prestec}")
    # SI ESCRIU 'RETORNAR', LI PREGUNTEM QUIN LLIBRE VOL RETORNAR
    elif resposta_accio == "retornar":
        llibre_retornar = input("Quin llibre vols retornar? ").capitalize()
        # SI EL NOM ES CORRECTE, AFEGIM +1 A L'ESTOC D'AQUEST LLIBRE
        if llibre_retornar in biblioteca.keys():
            autor = biblioteca[llibre_retornar][0]
            exemplars = biblioteca[llibre_retornar][1]
            biblioteca[llibre_retornar] = (autor, exemplars + 1)
            print("Moltes gràcies!")
        # SI ÉS UN LLIBRE QUE NO HI ÉS A LA BIBLIOTECA, LI DIEM QUE NO EL POT RETORNAR
        else:
            print("No pots retornar aquest llibre aquí.")
    else:
        print("Acció no vàlida.")

# QUAN L'USUARI ESCRIU 'SORTIR', MOSTREM LA BIBLIOTECA ACTUALITZADA
for llibre in biblioteca:
    print(f"{llibre} --- {biblioteca[llibre][0]} --- {biblioteca[llibre][1]}")