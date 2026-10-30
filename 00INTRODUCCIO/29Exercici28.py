# 8. Estadístiques de números aleatoris (Random + Llistes + Mètodes)

# Utilitza el mòdul random per generar una llista de 20 números enters aleatoris
# entre l'1 i el 100 de manera automàtica. Un cop generada la llista,
# calcula i imprimeix:

# El número més gran (fent servir funcions globals de Python com max()).
# El número més petit (min()).
# La mitjana de tots els números.
# Una subllista nova només amb els números parells utilitzant una llista per comprensió.

# IMPORTEM PER PODER GENERAR ELS NÚMEROS
import random

# CREEM LA LLISTA, DE MOMENT BUIDA
llista_numeros = []

# FEM UN BUCLE FOR FINS A 20 PER A QUE GENERI ELS 20 NÚMEROS I ELS GUARDI EN LA LLISTA
for i in range(20):
    llista_numeros.append(random.randint(1, 100))

print(llista_numeros)

# GUARDEM EN VARIABLES EL NÚMERO MÉS GRAN I EL MÉS BAIX
maxim = max(llista_numeros)
minim = min(llista_numeros)

# I ELS MOSTREM
print(f"Número més gran --- {maxim}")
print(f"Número més baix --- {minim}")

# CREEM UNA VARIABLE COMPTADOR I UN ALTRE PER FER LA SUMA
comptador = 0
suma_total = 0

# FEM UN ALTRE BUCLE FOR QUE REPASI LA LLISTA DE NÚMEROS I ELS VAGI SUMANT D'UN EN UN
# MENTRES EL COMPTADOR SUMA +1 EN CADA VOLTA
for num in llista_numeros:
    suma_total += num
    comptador += 1

# FEM UNA VARIABLE PER FER LA MITJANA I HO MOSTREM
mitjana = suma_total / comptador
print(f"Mitjana de tots els números --- {mitjana}")

# FEM UNA LLISA PER COMPRENSIÓ ON GUARDEM NOMÉS ELS NOMBRES PARELLS
num_parells = [x for x in llista_numeros if x % 2 == 0]
print(num_parells)