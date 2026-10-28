# 2. L'endevinalla del número secret

# Concepte: Bucle while, condicions, comptador, break.

# Enunciat: Defineix un número secret fix al codi (per exemple, 7).
# Fes un bucle while on demanis a l'usuari mitjançant input() que
# endevini el número (convertint-lo a int).

# Si l'usuari encerta, imprimeix un missatge de victòria amb un f-string
# dient quants intents has trigat i surt del bucle amb un break.

# Si falla, digues-li si el número secret és més alt o més baix, i torna
# a demanar-ho.

import random

numero_secret = random.randint(1, 10)

numero_input = int(input("Intenta endevinar el número del 1 al 10: "))
comptador = 1

while numero_input != numero_secret:
    if numero_input < numero_secret:
        numero_input = int(input("Error! El número secret es més ALT. Torna-ho a intentar: "))
        comptador += 1
    elif numero_input > numero_secret:
        numero_input = int(input("Error! El número secret és més BAIX. Torna-ho a intentar: "))
        comptador += 1

print(f"Enhorabona! Has encertat el número secret en {comptador} intents.\n"
      f"Era el: {numero_secret}")