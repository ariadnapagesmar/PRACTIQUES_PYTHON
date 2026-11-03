# 7. Afegir dades sense esborrar l'anterior (Modo "a") (Mitjà)

# Crea un fitxer anomenat registre.txt escrivint una línia. Després, crea un
# petit script que obri el fitxer en mode annex ("a" / append) per afegir una
# nova línia al final sense esborrar el text que ja hi havia escrit abans.
# Llegeix-ho al final per comprovar que hi ha les dues línies.

with open("registre.txt", "w") as arxiu:
    arxiu.write("Això és un registre.\n")

with open("registre.txt", "r") as arxiu:
    contingut = arxiu.read()
    print(contingut)

with open("registre.txt", "a") as arxiu:
    arxiu.write("Funcionarà això?")

with open("registre.txt", "r") as arxiu:
    contingut = arxiu.read()
    print(contingut)