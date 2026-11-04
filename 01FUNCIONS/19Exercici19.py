# 9. El comptador de visites persistent (Avançat)
from sys import exception

# Crea un programa que:

# Intenti llegir un número d'un fitxer anomenat visites.txt.
# Si el fitxer no existeix (primer cop), comenci a comptar des de 0.
# Sumi 1 a aquest comptador cada vegada que s'executa el programa.
# Guardi el nou valor actualitzat al mateix fitxer abans d'acabar.
# (Resultat: cada cop que prem 'Run' a PyCharm, el programa dirà "Aquesta és
# la teva visita número X").

# FEM UN TRY - EXCEPT PER SI ENS SALTA L'ERROR DE QUE NO EXISTEIX EL FILE
try:
    # LI DIEM AL PROGRAMA QUE PROVI D'OBRIR EL FILE PER LLEGIR I GUARDEM
    # EL CONTINGUT DE DINS EN UNA VARIABLE
    with open("visites.txt", "r") as arxiu:
        contingut = arxiu.read().strip()

        # SI CONTINGUT EXISTEIX I NO ESTÀ BUIT, LI SUMEM 1 A LA VARIABLE
        # VISITES, QUE CONTARÀ QUANTS COPS EXECUTEM EL PROGRAMA
        if contingut:
            visites = int(contingut) + 1
        # SI NO EXISTEIX, VISITES COMENÇA PER 0
        else:
            visites = 0

# SI NO ES TROBA CAP FILE, VISITES TAMBÉ COMENÇARÀ PER 0
except FileNotFoundError:
    visites = 0

# OBRIM EL FILE UN ALTRE COP FORA DEL TRY - EXCEPT, PERÒ AQUEST COP PER
# ESCRIURE I LI PASSEM LA VARIABLE 'VISITES'
with open("visites.txt", "w") as arxiu:
    arxiu.write(str(visites))

# MOSTREM PER CONSOLA EL CONTINGUT DEL FILE, QUE SON LES VEGADES QUE
# HA EXECUTAT EL PROGRAMA
print(f"Aquesta es la teva visita número {visites}")