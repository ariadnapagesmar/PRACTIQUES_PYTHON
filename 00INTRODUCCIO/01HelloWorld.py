print("Hello world!")

# OPERADORS ARITMETICS (exemple)

# a = 10
# b = 3

# suma = a + b   # 13
# resta = a - b    # 7
# multiplicacion = a * b    # 30
# division = a / b   # 3.333333333
# división_entera = a // b   # 3
# modulo = a % b   # 1
# exponenciacion = a ** b   # 1000

# OPERADORS DE COMPARACIO (exemple)

# a = 10
# b = 3

# igual = a == b   # False
# diferente = a != b   # True
# mayor que = a > b   # True
# menor que = a < b   # False
# mayor o igual = a >= b   # True
# menor o igual = a <= b   # False

# OPERADORS LOGICS (exemple)

# a = 10
# b = 3

# resultado_and = (a > 5) and (b < 5)   # True
# resultado_or = (a > 15) or (b < 5)   # True
# resultado_not = not (a > 5)   # False


# LLISTA DE MÈTODES I FUNCIONS PER A STRINGS

# len(text): Retorna la longitud (nombre total de caràcters) del text.
# (Nota: len() és una funció global, no s'escriu amb un punt davant).

# .upper(): Converteix tots els caràcters del text a majúscules.

# .lower(): Converteix tots els caràcters del text a minúscules.

# .capitalize(): Posa només la primera lletra de la frase o paraula en majúscula i la resta en minúscules.

# .title(): Posa la primera lletra de cada paraula en majúscula.

# .count(sub): Compta quantes vegades apareix un caràcter o una subcadena (sub) concreta dins del text.
# Exemple: "patata".count("a") retorna 3.

# .find(sub): Retorna la posició (l'índex numèric) on comença per primera
# vegada la subcadena buscadada. Si no la troba, retorna -1.

# .replace(vell, nou): Substitueix totes les aparicions d'una part del text per una altra nova.
# Exemple: "Hola Món".replace("Món", "Python") dóna "Hola Python".

# .strip(): Elimina automàticament els espais en blanc sobrants que hi hagi al principi
# i al final del text (molt útil quan llegeixes dades amb input()).

# .split(separador): Divideix un text en una llista de subcadenes utilitzant el
# caràcter separador que li indiquis (per defecte separa per espais).
# Exemple: "vermell,blau,verd".split(",") dóna ["vermell", "blau", "verd"].

# zip(): Aquesta funció s'encarrega d'"aparellar" els elements de tantes llistes
# com li passis en forma de tuples.
# EXEMPLE:

noms = ["  anna garcia ", "PERE martínez ", "  joan    PaMpIn", " arI pagES     "]
sous = [1900, 1200, 2500, 2100]

# Utilitzem zip(noms, sous) per unir les dues llistes en parelles (nom, sou)
# I aplicarem .strip().title() al nom per netejar-lo
noms_sous = [(nom.strip().title(), sou) for nom, sou in zip(noms, sous) if sou > 1500]

print(noms_sous)


# IF (exemple)

edad1 = 18

if edad1 >= 18:
   print ("Eres mayor de edad.")


# IF-ELSE (exemple)

edad2 = 15

if edad2 >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")


# IF-ELIF-ELSE (exemple)

calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")


# FOR (exemple)

frutas1 = ["manzana", "banana", "naranja"]

for fruta in frutas1:
    print(fruta)


# WHILE (exemple)

contador1 = 0

while contador1 < 5:

    print(contador1)
    contador1 += 1


# BREAK (exemple)

contador2 = 0

while True:

    print(contador2)
    contador2 += 1

    if contador2 == 5:
        break


# CONTINUE (exemple)

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)


# LLISTES (exemple)

frutas2 = ["manzana", "banana", "naranja"]

print(frutas2[0])  # Imprime "manzana"
print(frutas2[1])  # Imprime "banana"
print(frutas2[2])  # Imprime "naranja"


# METODES DE LLISTES (exemple)

frutas2.append("pera")
print(frutas2)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas2.insert(1, "uva")
print(frutas2)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas2.remove("banana")
print(frutas2)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas2.pop(2)
print(frutas2)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas2.sort()
print(frutas2)  # Imprime ["manzana", "pera", "uva"]

frutas2.reverse()
print(frutas2)  # Imprime ["uva", "pera", "manzana"]


# CÀLCULS DINS DE LLISTES (exemple)

numeros1 = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros1 if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]


# TUPLES (exemple)

# A diferencia de les llistes, les tuples son inmutables, el que significa que no es poden 
# modificar un cop creades. No es poden afegir, eliminar o canviar elements en una tupla existent.

# Per crear una tupla, tanca els elements entre parèntesi:

punto = (3, 4)

print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

# MÈTODES DE LES TUPLES

# .count(element)
# Compta quantes vegades apareix un element determinat dins de la tupla.
colors = ("vermell", "blau", "verd", "blau", "groc", "blau")

# Compta quantes vegades surt la paraula "blau"
repes = colors.count("blau")
print(repes)  # Imprimeix 3

# .index(element)
# Busca un element i et retorna la posició (l'índex numèric) de la primera vegada que apareix.
colors = ("vermell", "blau", "verd", "groc")

# On es troba "verd"?
posicio = colors.index("verd")
print(posicio)  # Imprimeix 2 (recorda que es comença a comptar des del 0)


# DICCIONARIS (exemple)

# Un diccionari es una estructura de dades mutables i no ordenades que permet emmagarzemar parelles de clau-valor. 
# Cada element en un diccionari consisteix en una clau única i el seu valor corresponent. Els diccionaris es
# tanquen entre claus {}, y les parelles clau-valor es separen per comes.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"


# METODES DE DICCIONARIS (exemple)

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}


# CONJUNTS(SETS) (exemple)

# Un conjunt es una estructura de dades mutable i no ordenada que permet emmagatzemar una col·lecció 
# d'elements únics. Els conjunts es tanquen entre claus {} o es creen utilitzant la funció set().
# La principal diferència amb la resta de tipus de llistes es que un conjunt serveix principalment
# per a realitzar operacions de teoria de conjunts, com la unió, la intersecció i la diferència.

frutas3 = {"manzana", "banana", "naranja"}
numeros2 = set([1, 2, 3, 4, 5])

# Els conjunts admeten operacions matemàtiques de conjunts, com la unió (|), la intersecció (&), 
# la diferencia (-) y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}


# METODES DE CONJUNTS (exemple)

frutas3.add("pera")
print(frutas3)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas3.remove("banana")
print(frutas3)  # Imprime {"manzana", "naranja", "pera"}

frutas3.discard("uva")
print(frutas3)  # Imprime {"manzana", "naranja", "pera"}

frutas3.clear()
print(frutas3)  # Imprime set()


# EL EQUIVALENT A L'SCANNER DE JAVA: INPUT (exemple)

# Hi ha un petit detall molt important que ve de Java: input() sempre retorna un text (string), 
# per molt que l'usuari escrigui un número. Per tant, si després vols comparar-lo amb un nombre, 
# l'has de convertir a enter (int()) o decimal (float()).

# Demanem a l'usuari que introdueixi un valor i el convertim a decimal (float)
temperatura = float(input("Introdueix la temperatura actual: "))

if temperatura >= 25:
    print("Fa calor")
else:
    print("Fa fresca o fred")


# F-STRING (exemple)

# Un f-string (de formatted string-literal) és una eina de Python 
# per inserir variables i operacions directament dins d'un text de 
# manera molt neta i visual, sense haver de patir per concatenar 
# amb + ni convertir tipus de dades.

# Funciona amb només dos passos:

# 1. Poses una lletra f (o F) just davant de les cometes del text.
# 2. Dins del text, poses qualsevol variable o operació matemàtica tancada entre claus {}.

nom = "Laura"
edat = 28

# Posem la 'f' davant i les variables entre {}
missatge = f"Hola, em dic {nom} i tinc {edat} anys."

print(missatge)
# Imprimeix: Hola, em dic Laura i tinc 28 anys.


# RANDOM (exemple)

import random

# Genera un número enter aleatori entre l'1 i el 10 (ambdós inclosos)
numero_aleatori = random.randint(1, 10)

print(f"El número enter aleatori generat és: {numero_aleatori}")

# Com funciona?

# import random: Importa el paquet de funcions aleatòries de Python
# (això s'acostuma a posar a la línia de dalt de tot del teu fitxer .py).
# random.randint(a, b): Retorna un nombre enter (int) escollit a
# l'atzar dins del rang tancat entre a i b (és a dir, inclou tant el
# límit inferior com el superior).

import random

# Genera un número decimal (float) aleatori entre l'1.0 i el 10.0
numero_aleatori = random.uniform(1.0, 10.0)

print(f"El número decimal aleatori generat és: {numero_aleatori}")
