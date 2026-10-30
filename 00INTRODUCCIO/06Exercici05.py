# 5. Utilitzar break en un bucle infinit

# Concepte: while True, break.

# Enunciat: Escriu un bucle while True que comenci amb un comptador a 0. 
# A cada volta, incrementa el comptador en 1 i imprimeix-lo. 
# Fes servir un break per sortir automàticament del bucle quan el comptador arribi a 7.

comptador1 = 0

while comptador1 < 7:
    print(comptador1)
    comptador1 += 1

comptador2 = 0

while True:
    print(comptador2)
    comptador2 += 1
    if comptador2 == 7:
        break