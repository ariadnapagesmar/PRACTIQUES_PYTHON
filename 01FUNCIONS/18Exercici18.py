# 8. Llistar i comptar línies d'un fitxer (Mitjà)

# Crea un fitxer de text amb 4 o 5 noms de ciutats (un per línia). Fes un programa
# que llegeixi el fitxer línia a línia, netegi els salts de línia amb .strip(),
# imprimeixi cada ciutat numerada (1. Barcelona, 2. Madrid...) i al final digui
# quantes ciutats hi havia en total.

with open("ciutats.txt", "w") as arxiu:
    arxiu.write("Barcelona\n"
                "Madrid\n"
                "Bilbao\n"
                "Sevilla\n"
                "Reus")

comptador = 1
total_ciutats = 0

with open("ciutats.txt", "r") as arxiu:
    for linia in arxiu:
        ciutat = linia.strip()
        if linia:
            print(f"{comptador}. {ciutat}")
        comptador += 1
        total_ciutats += 1

print(f"Hi ha {total_ciutats} ciutats en total.")