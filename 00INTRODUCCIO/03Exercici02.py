# 2. Descompte al cinema (if-elif-else i operadors lògics)

# Concepte: if-elif-else, operadors lògics (and, or).

# Enunciat: Imagina que vols calcular el preu d'una entrada segons 
# l'edat i si dissenyes o no d'un carnet de soci.

# Si l'edat és menor de 18 o tens carnet de soci (soci == True), 
# imprimeix "Tens descompte jove/soci".
# Si tens 65 anys o més, imprimeix "Tens descompte de jubilat".
# En qualsevol altre cas, imprimeix "Preu general".

edat = int(input("Quina edat tens?"))
carnetSoci = input("Tens carnet de soci? (si/no)").lower()

soci = False

if carnetSoci == "si":
    soci = True
else:
    soci = False

if edat < 18 or soci == True:
    print("Tens descompte jove o de soci!")
elif edat >= 65:
    print("Tens descompte de jubilat!")
else:
    print("Preu general")