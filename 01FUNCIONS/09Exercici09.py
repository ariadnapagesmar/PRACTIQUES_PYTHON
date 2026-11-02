# 9. El joc d'endevinar el número amb funcions modulars (Avançat)

# Utilitza el mòdul random i construeix un joc on s'hi jugui a través de funcions:

# Una funció genera_secret() que retorni un enter aleatori entre l'1 i el 50.
# Una funció comprova_int(intent, secret) que retorni "més petit", "més gran"
# o "igual!".
# El programa principal ha de gestionar el bucle while d'intents de l'usuari
# cridant aquestes funcions.

# IMPORTEM PER PODER GENERAR NÚMEROS RANDOM
import random

# CREEM UNA FUNCIÓ QUE GENERI EL NÚMERO RANDOM ENTRE 1 I 50
def genera_secret():
    return random.randint(1, 50)

# CREEM UNA FUNCIÓ QUE COMPARI EL NÚMERO QUE ESCRIGUI L'USUARI I EL NÚMERO SECRET
# ESCRIU SI EL NÚMERO DE L'USUARI ÉS MÉS GRAN, MÉS PETIT O IGUAL QUE EL SECRET
def comprova_int(intent, secret):
    if intent < secret:
        return "més gran"
    elif intent > secret:
        return "més petit"
    elif intent == secret:
        return "igual!"

# GENEREM EL NÚMERO
secret = genera_secret()

# LI DIEM A L'USUARI QUE INTENTI ENDEVINAR EL NÚMERO SECRET I GUARDEM LA RESPOSTA
intent = int(input("Intenta esbrinar el número secret (1-50): "))

# CREEM UN BUCLE QUE CONTINUI SEMPRE I QUAN EL NÚMERO QUE ESCRIGUI L'USUARI NO
# SIGUI IGUAL QUE EL NÚMERO SECRET, CRIDANT A LA FUNCIÓ PER A QUE COMPARI ELS NÚMEROS
while intent != secret:
    resultat = comprova_int(intent, secret)

    # CANVIEM EL TEXT I LI EXPLIQUEM A L'USUARI SI EL NÚMERO SECRET ÉS MÉS PETIT O
    # MÉS GRAN QUE EL NÚMERO QUE ELL HA ESCRIT
    if resultat == "més gran":
        print(f"El número secret és més gran que {intent}")
    elif resultat == "més petit":
        print(f"El número secret és més petit que {intent}")

    intent = int(input("Torna-ho a provar (1-50): "))

# SI HO ENDEVINA, SURT DEL BUCLE I SALTA AQUÍ
print(f"Enhorabona! Has esbrinat el número secret. Era el: {secret}")