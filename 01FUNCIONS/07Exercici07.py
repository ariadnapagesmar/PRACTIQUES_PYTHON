# 7. Agenda de contactes encapsulada en funcions (Avançat)

# Refactoritza (passa a format de funcions) el teu programa de l'agenda de
# contactes que has fet abans.

# Crea com a mínim dues funcions:
# afegir_contacte(agenda, nom, telefon): Modifica el diccionari afegint la dada.
# consultar_contacte(agenda, nom): Retorna el telèfon si existeix o un avís si no hi és.

# Després, munta el bucle while principal que cridi aquestes funcions segons
# el que triï l'usuari.

# CREEM UN DICCIONARI BUIT, QUE SERÀ L'AGENDA DE CONTACTES
agenda = {}


# CREEM LA FUNCIÓ PER AFEGIR CONTACTES I SIMPLEMENT AFEGIM EL NOM I EL NÚMERO DE
# TELÈFON A L'AGENDA I ESCRIVIM UN MISSATGE DIENT QUE S'HA AFEGIT AMB ÉXIT
def afegir_contacte(agenda, nom, telefon):
    agenda[nom] = {telefon}
    print("Contacte afegit amb èxit.")

# CREEM LA FUNCIÓ PER BUSCAR UN CONTACTE A L'AGENDA. FEM UN BUCLE QUE BUSQUI NOM PER
# NOM AMB agenda.keys(), JA QUE ELS NOMS SON LES CLAUS DEL DICCIONARI I EL MOSTREM
# AMB EL NÚMERO DE TELÈFON CORRESPONENT. SI EL CONTACTE NO HI ÉS A L'AGENDA, HO DIEM
# TAMBÉ AMB UN MISSATGE
def consultar_contacte(agenda, nom):
    if nom in agenda.keys():
        print(f"{nom} --- {agenda[nom]}")
    else:
        print("Aquest contacte no existeix en la teva agenda.")

# PREGUNTEM QUINA ACCIÓ VOL FER L'USUARI
accio_usuari = input("Ets a la teva agenda personal. "
                     "Vols afegir (1), consultar (2) o sortir (3)? ")

# MENTRES NO ESCRIGUI '3', QUE ÉS EL NÚMERO PER SORTIR, EL BUCLE CONTINUARÀ
while accio_usuari != "3":
    # SI ESCRIU '1' PER AFEGIR UN CONTACTE, LI DEMANEM EL NOM DEL CONTACTE QUE VOL
    # AFEGIR I EL NÚMERO DE TELÈFON. CRIDEM LA FUNCIÓ I FIQUEM COM PARÀMETRES L'AGENDA,
    # EL NOM I TELÈFON EN QUESTIÓ
    if accio_usuari == "1":
        nom = input("Escriu el nom del contacte que vols afegir: ").capitalize()
        telefon = input("Escriu el número de telèfon del teu contacte: ")
        afegir_contacte(agenda, nom, telefon)
        accio_usuari = input("Continues en la teva agenda personal. "
                             "Vols afegir (1), consultar (2) o sortir (3)? ")
    # SI L'USUARI ESCRIU '2' PER CONSULTAR L'AGENDA, LI DEMANEM EL NOM DEL CONTACTE
    # QUE VOL BUSCAR. CRIDEM LA FUNCIÓ I PASSEM COM A PARÀMETRE L'AGENDA I EL NOM
    # EN QUESTIÓ
    elif accio_usuari == "2":
        nom = input("Escriu el nom del contacte que vols buscar en la teva agenda: ").capitalize()
        consultar_contacte(agenda, nom)
        accio_usuari = input("Continues en la teva agenda personal. "
                             "Vols afegir (1), consultar (2) o sortir (3)? ")
    # SI L'USUARI ESCRIU ALGO QUE NO SIGUI '1, 2 O 3', AVISEM QUE L'ACCIÓ NO ÉS VÀLIDA
    # I TORNEM A PREGUNTAR
    else:
        accio_usuari = input("Acció no vàlida. Vols afegir (1), consultar (2) o sortir (3)? ")

print("Gràcies per utilitzar la teva agenda personal. Adéu.")

