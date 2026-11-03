# 6. El mètode modern with open (Mitjà)

# Reescriu l'exercici 3 i 4 utilitzant la paraula clau with (per exemple:
# with open("notes.txt", "w") as arxiu:). Escriu-hi tres línies de text
# (per exemple, tres fruites) i comprova com no fa falta escriure .close(),
# Python s'encarrega de tancar-ho sol de manera segura.

with open("notes.txt", "w") as arxiu:
    arxiu.write("Plàtan.\n"
                "Poma.\n"
                "Cirera.\n")

with open("notes.txt", "r") as arxiu:
    contingut = arxiu.read()
    print(contingut)
