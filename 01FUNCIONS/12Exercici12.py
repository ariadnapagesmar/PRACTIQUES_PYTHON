# 2. Validar l'entrada de text a número (Fàcil)

# Demanar a l'usuari que introdueixi la seva edat mitjançant un input(). Utilitza
# un bloc try-except per capturar l'error ValueError (per si l'usuari escriu
# lletres com "dotze" en comptes d'un número). Si s'equivoca, avisa'l; si ho fa bé,
# mostra un missatge amb l'edat introduïda.

try:
    edat = int(input("Escriu la teva edat: "))
    print(f"La teva edat és: {edat}")
except ValueError:
    print("No pot escriure la teva edat així. Ha de ser un número ENTER.")
