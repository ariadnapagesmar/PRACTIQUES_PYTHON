# 5. Simulador d'un caixer automàtic amb límits d'intents (While + Condicionals)

# Programa un caixer automàtic amb un PIN secret preestablert (per exemple, "1234").
# L'usuari té un màxim de 3 intents per encertar-lo. Si s'equivoca 3 cops, el compte
# queda blocat i el programa s'atura. Si l'encerta, entra a un menú interactiu on pot
# consultar el saldo o sortir.

# IMPORTEM PER PODER GENERAR NÚMEROS RANDOM
import random

# ESTABLIM UN PIN I UN COMPTADOR DE 3 INTENTS
pin = 1234
comptador = 3
resposta_pin = ""

# OBRIM UN BUCLE, S'ATURA QUAN EL COMPTADOR D'INTENTS PER FICAR EL PIN ARRIBA A 0
while comptador > 0 and resposta_pin != pin:
    resposta_pin = int(input(f"Escriu el PIN de 4 dígits. Tens {comptador} intens: "))
    comptador -= 1
    # SI L'USUARI ESCRIU BÉ EL PIN, ENTRE EN EL MENÚ INTERACTIU
    if resposta_pin == pin:
        print("PIN correcte.")
        resposta_compte = ""
        # OBRIM UN ALTRE BUCLE QUE S'ATURA QUAN L'USUARI ESCRIU 'SORTIR'
        while resposta_compte != "sortir":
            resposta_compte = input("Benvingut al teu compte bancari. Escriu 'saldo' si vols "
                                    "consultar els diners que tens, o 'sortir' si ja has acabat: ").lower()
            # SI L'USUARI ESCRIU 'SALDO', LI MOSTREM UN SOU GENERAT PEL RANDOM
            if resposta_compte == "saldo":
                saldo = round(random.uniform(1.0, 1000000.0), 2)
                print(f"El teu saldo és de {saldo} euros.")
            # MISSATGE SI L'USUARI ESCRIU 'SORTIR'
            elif resposta_compte == "sortir":
                print("Gràcies per utilitzar el nostre caixer. Adéu.")
            # MISSATGE SI L'USUARI ESCRIU UNA ACCIÓ NO VÀLIDA
            else:
                print("No pots fer aquesta acció. Seràs redirigit al menú principal: ")
    else:
        print("PIN equivocat.")
        # MISSATGE SI L'USUARI ES QUEDA SENSE INTENTS
        if comptador == 0:
            print("T'has quedat sense intents. El compte ha quedat bloquejat.")
