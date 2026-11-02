# 6. Estadístiques flexibles amb nombre variable d'arguments (*args) (Mitjà)

# Crea una funció anomenada analitza_numeros(*valors) que pugui acceptar una
# quantitat variable de números enters. La funció ha de retornar una tupla amb
# tres valors: la suma total, la quantitat de números que s'han passat, i la
# mitjana aritmètica. Crida-la passant-li diferents quantitats de nombres en cada prova.

# CREEM LA FUNCIÓ I PASSEM UNA VARIABLE AMB * AL DAVANT PER PASSAR-LI DESPRÉS
# UNA LLISTA DE DIFERENTS VALORS
def analitza_numeros(*valors):
    suma_total = 0
    comptador = 0
    # OBRIM UN BUCLE QUE SUMI TOTS ELS NÚMEROS I SUMI 1 AL COMPTADOR PER CADA NÚMERO
    # PASSAT. FEM LA MITJANA I REOTRNEM LES TRES DADES COM UNA TUPLA
    for numero in valors:
        suma_total += numero
        comptador += 1
    mitjana = suma_total / comptador
    return (suma_total, comptador, mitjana)

# CRIDEM LA FUNCIÓ I LI PASSEM OCM A PARÀMETRES ELS NÚMEROS QUE VOLGUEM
print(analitza_numeros(1, 2, 3))
print(analitza_numeros(4, 5, 6, 7))
print(analitza_numeros(10, 22, 14, 50))