# Exercici 2: Propietats amb @property (L'estil Pythonic)

# Enunciat: Reprèn una classe CompteBancari o crea'n una de nova amb un
# saldo privat __saldo. Utilitza els decoradors @property i @saldo.setter
# per controlar que ningú pugui posar un saldo negatiu directament des de fora
# (si intenten assignar un nombre negatiu, llança un ValueError).

# CREEM LA CLASE CompteBancari I LI AFEGIM EL ATRIBUT SALDO COM PRIVAT
class CompteBancari:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # CREEM EL GETTER FÀCILMENT AMB EL @PROPERTY
    @property
    def saldo(self):
        return self.__saldo

    # CREEM EL SETTER, PERÒ NOMÉS CANVIARÀ EL SALDO SI NO ÉS UN NÚMERO NEGATIU,
    # SINO SALTA UN ValueError
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("No pots ficar un saldo negatiu!")
        else:
            self.__saldo = saldo

# CREEM EL COMPTE BANCARI PER FER LES PROVES
compte_bancari = CompteBancari("Ariadna Pagès", 10000)

# EL GETTER IMPRIMEIX EL SALDO ACTUAL
print(compte_bancari.saldo)

# FEM UN TRY...EXCEPT PER PROVAR SI ÉS L'USUARI HA ESCRIT UN SALDO NO NEGATIU
try:
    compte_bancari.saldo = int(input("Escriu el teu saldo: "))

except ValueError as e:
    print(e)

# IMPRIMIM EL SALDO UN ALTRE COP
print(compte_bancari.saldo)