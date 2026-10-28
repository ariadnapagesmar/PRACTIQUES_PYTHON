# 7. Cercador de capitals en Diccionari

# Concepte: Diccionaris, input(), mètodes .keys(), comprovació de claus.

# Enunciat: Crea un diccionari amb almenys 4 països i les seves capitals
# (p.ex., {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma", "Portugal": "Lisboa"}).

# Demana a l'usuari mitjançant input() que introdueixi el nom d'un país.

# Comprova si el país està dins de les claus del diccionari
# (p.ex., fent if pais in diccionari:). Si hi és, imprimeix la seva capital
# amb un f-string. Si no hi és, mostra un missatge d'error dient que no el
# tens registrat.

paisos = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma", "Portugal": "Lisboa"}

resposta = input("Escriu el nom d'un pais: ").capitalize()

if resposta in paisos:
    print(paisos[resposta])
else:
    print(f"El pais {resposta} no està registrat.")