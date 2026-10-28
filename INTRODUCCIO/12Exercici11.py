# 1. Calculadora d'IMC (Índex de Massa Corporal)

# Concepte: input(), conversions (float), operadors aritmètics, if-elif-else, f-strings.

# Enunciat: Fes un programa que demani a l'usuari el seu pes en kilograms (p.ex. 70.5) i
# la seva altura en metres (p.ex. 1.75). Calcula l'IMC amb la fórmula:
# pes / (altura^2). Utilitza un if-elif-else per classificar el resultat:
# Menys de 18.5: "Pes baix"
# Entre 18.5 i 24.9: "Pes normal"
# 25 o més: "Sobrepès"
# Imprimeix el resultat final utilitzant un f-string que mostri el valor
# de l'IMC arrodonit o directe.

pes = float(input("Escriu el teu pes en kg: "))
altura = float(input("Escriu la teva alçada en metres: "))

imcCalcul: float | int = pes / (altura ** 2)

imcResultat = ""

if imcCalcul < 18.5:
    imcResultat = "Pes baix"
elif 18.5 <= imcCalcul < 25:
    imcResultat = "Pes normal"
else:
    imcResultat = "Sobrepès"

print(f"Pes: {pes}\n"
      f"Altura: {altura}\n"
      f"Resultat IMC: {imcCalcul}\n"
      f"{imcResultat}")