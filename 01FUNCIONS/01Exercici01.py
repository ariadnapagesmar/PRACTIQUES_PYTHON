# 1. La salutació personalitzada (Fàcil)

# Crea una funció anomenada saluda_usuari que accepti dos paràmetres: el nom de
# la persona i l'hora del dia (un número enter de 0 a 23). La funció ha de
# retornar (amb return) un text tipus: "Bon dia, Anna!" si l'hora és menor
# de 12, "Bona tarda, Anna!" si és menor de 20, o "Bona nit, Anna!" en cas contrari.
# Crida-la des de fora i imprimeix el resultat.

# CREEM LA FUNCIÓ saluda_usuari I FIQUEM COM A PARÀMETRES EL NOM I L'HORA
def saluda_usuari(nom, hora):
    # SI SON ENTRE LES 5 DE LA MATINADA I LES 12 DEL MIGDIA, DIEM 'BON DIA'
    if 5 <= hora < 12:
        print(f"Bon dia, {nom}!")
    # SI SON ENTRE LES 12 DEL MIGDIA I LES 20 DE LA NIT, DIEM 'BONA TARDA'
    elif 12 <= hora < 20:
        print(f"Bona tarda, {nom}!")
    # SI SON ENTRE LES 20 I LES 00 DE LA NIT, O ENTRE LES 00 I LES 5 DE LA
    # MATINADA, DIEM 'BONA NIT'
    elif (20 <= hora < 24) or (0 <= hora < 5):
        print(f"Bona nit, {nom}!")
    # SI FICA UNA HORA FORA DELS PARÀMETRES D'AMUNT, DIEM UNA RESPOSTA AMBÍGUA
    else:
        print(f"Bona vida, {nom}.")

# DEMANEM EL NOM I L'HORA DE L'USUARI
nom = input("Escriu el teu nom: ")
hora = int(input("Escriu quina hora és: "))

# CRIDEM LA FUNCIÓ AMB EL NOM I L'HORA QUE HEM DEMANAT A L'USUARI
saluda_usuari(nom, hora)