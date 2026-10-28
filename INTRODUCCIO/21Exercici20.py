# 10. Mini-Directori de Contactes (Diccionari avançat)

# Concepte: Diccionaris mutables, input(), f-strings, estructures niades
# o actualització de dades.

# Enunciat:
# Crea un programa de gestió de contactes:
# Comença amb un diccionari buit anomenat agenda.

# Fes un bucle while que doni a triar a l'usuari (mitjançant un input) si vol
# "afegir" un contacte o "consultar" un contacte (o escriure "sortir" per acabar).

# Si escriu "afegir": demana el nom del contacte i el seu telèfon, i guarda-ho
# al diccionari.

# Si escriu "consultar": demana el nom del contacte i, si existeix a l'agenda,
# mostra el seu telèfon amb un f-string. Si no existeix, avisa a l'usuari.

# CREEM EL DICCIONARI BUIT
agenda = {}

# PREGUNTEM QUINA ACCIÓ VOL FER L'USUARI I LA GUARDEM EN UNA VARIABLE
resposta_usuari = input("Ets a la teva agenda personal. "
                        "Vols afegir, consultar o sortir?").lower()

# COMPROVEM QUE LA RESPOSTA ÉS VÀLIDA I SI NO HO ÉS LA TORNEM A PREGUNTAR EN BUCLE
# FINS QUE CONTESTI BÉ O ESCRIGUI 'SORTIR'
while resposta_usuari != "afegir" and resposta_usuari != "consultar" and resposta_usuari != "sortir":
    print("Aquesta acció no es vàlida.")
    resposta_usuari = input("Vols afegir, consultar o sortir?").lower()

# SI RESPON BÉ, COMPROVEM QUE ESTÀ REALMENT BÉ I QUE NO HAGI ESCRIT 'SORTIR' TAMPOC
while resposta_usuari != "sortir" and (resposta_usuari == "afegir" or resposta_usuari == "consultar"):
    # SI ESCRIU 'AFEGIR', LI DEMANEM EL NOM I EL NÚMERO I EL GUARDEM DINS DE L'AGENDA
    if resposta_usuari == "afegir":
        nom_nou = input("Escriu el nom del nou contacte: ").capitalize()
        numero_telf_nou = input("Escriu el numero de telefon del nou contacte: ")
        agenda[nom_nou] = {numero_telf_nou}

        # TORNEM A PREGUNTAR QUINA ACCIÓ VOL FER I COMPROVEM QUE ESTÀ BÉ
        resposta_usuari = input("Continues en la teva agenda personal. "
                                "Vols afegir, consultar o sortir?").lower()
        while resposta_usuari != "afegir" and resposta_usuari != "consultar" and resposta_usuari != "sortir":
            print("Aquesta acció no es vàlida.")
            resposta_usuari = input("Vols afegir, consultar o sortir?").lower()

    # SI ESCRIU 'CONSULTAR', LI DEMANEM EL NOM DEL CONTACTE QUE VOL BUSCAR I LI MOSTREM EL TELF
    elif resposta_usuari == "consultar":
        nom = input("Escriu el nom del teu contacte: ").capitalize()
        if nom in agenda:
            print(f"El telèfon de {nom} és: {agenda[nom]}")
        else:
            print("Aquest contacte no existeix en la teva agenda.")

        # TORNEM A PREGUNTAR QUINA ACCIÓ VOL FER I COMPROVEM SI ESTÀ BÉ
        resposta_usuari = input("Continues en la teva agenda personal. "
                                    "Vols afegir, consultar o sortir?").lower()
        while resposta_usuari != "afegir" and resposta_usuari != "consultar" and resposta_usuari != "sortir":
            print("Aquesta acció no es vàlida.")
            resposta_usuari = input("Vols afegir, consultar o sortir?").lower()


print(agenda)