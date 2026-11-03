# 1. Evitar la divisió per zero (Fàcil)

# Escriu un programa que demani a l'usuari un número enter, el divideixi per 10
# (és a dir, 10 / numero) i imprimeixi el resultat. Protegeix el codi amb un
# try-except perquè, si l'usuari escriu el 0, el programa no peti sinó que
# imprimeixi un avís amable ("No es pot dividir per zero!").

numero = int(input("Escriu un número: "))

try:
    divisio = 10 / numero
    print(f"El resultat de 10 / {numero} és = {divisio}")
except ZeroDivisionError:
    print("No es pot dividir per zero!")
