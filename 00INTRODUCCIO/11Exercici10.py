# 10. Llistes per comprensió (List Comprehensions)

# Concepte: [x for x in ... if ...].

# Enunciat: Partint d'una llista de nombres del 1 al 10
# (numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), utilitza una llista
# per comprensió per crear una nova llista que contingui només els
# cubs (x^3) d'aquells nombres que siguin senars. Imprimeix el resultat.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numerosElevatsAlCub = [x ** 3 for x in numeros if x % 2 != 0]

print(numerosElevatsAlCub)

for numero in numerosElevatsAlCub:
    print(numero)
