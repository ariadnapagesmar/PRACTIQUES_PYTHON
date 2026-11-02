# 2. Calculadora d'àrees amb valors de retorn (Fàcil)

# Escriu tres funcions diferents:
# Una que calculi l'àrea d'un quadrat (area_quadrat(costat)).
# Una altra per al cercle (area_cercle(radi), pots fer servir 3.1416 * radi ** 2).
# Una altra per al triangle (area_triangle(base, altura)).

# Fes un petit programa interactiu amb input() on l'usuari triï quina figura
# vol calcular, demani les dades necessàries, cridi la funció corresponent
# i mostri el resultat.

# CREEM UNA FUNCIÓ PER CALCULAR L'ÀREA DEL QUADRAT
def area_quadrat(costat):
    return costat * costat

# CREEM UNA ALTRA FUNCIÓ PER CALCULAR L'ÀREA DEL CERCLE
def area_cercle(radi):
    return 3.1416 * (radi ** 2)

# CREEM UNA ALTRA FUNCIÓ PER CALCULAR L'ÀREA DEL TRIÀNGLE
def area_triangle(base, altura):
    return (base * altura) / 2

# LI PREGUNTEM A L'USUARI QUINA FIGURA VOL CALCULAR
resposta_usuari = input("De quina figura vols calcular l'àrea?\n"
      "Quadrat (1), Cercle (2) o Triàngle (3)?")

# CREEM UN IF, ELIF ON CRIDEM UN MÈTODE O ALTRE EN FUNCIÓ DE LA RESPOSTA D'ABANS
if resposta_usuari == "1":
    costat = float(input("Escriu la longitud del quadrat en centímetres: "))
    print(f"L'àrea del quadrat és: {area_quadrat(costat)}cm2")
elif resposta_usuari == "2":
    radi = float(input("Escriu el radi del cercle en centímetres: "))
    print(f"L'àrea del cercle és: {area_cercle(radi)}cm2")
elif resposta_usuari == "3":
    base = float(input("Escriu la longitud de la base del triàngle en centímetres: "))
    altura = float(input("Escriu l'alçada del tràngle en centímetres: "))
    print(f"L'àrea del triàngle és: {area_triangle(base, altura)}cm2")
else:
    print("Incorrect input")