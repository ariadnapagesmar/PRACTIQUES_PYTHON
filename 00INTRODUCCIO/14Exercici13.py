# 3. Suma acumulativa amb filtre (continue i break)

# Concepte: while True, continue, break, acumuladors.

# Enunciat: Crea un programa que demani números enters a l'usuari de manera
# indefinida (while True).

# Si l'usuari introdueix un número negatiu, l'has d'ignorar utilitzant continue.

# Si l'usuari introdueix el 0, el programa ha de sortir del bucle amb break.

# Per a qualsevol altre número positiu, ves sumant-lo a un acumulador total.
# Al final, quan s'aturi, imprimeix la suma total acumulada amb un f-string.

suma_numeros = 0

while True:
    numero = int(input("Introdueix un número: "))

    if numero < 0:
        continue
    elif numero == 0:
        break
    else:
        suma_numeros += numero

print(f"Suma total: {suma_numeros}")