# Exercici 3: Modificar atributs des de fora

# Objectiu: Entendre que els atributs poden canviar.
# Enunciat: Crea una classe anomenada CompteBancari que tingui els atributs
# titular i saldo (el saldo inicial pot ser 0.0 per defecte). Crea un objecte,
# imprimeix el saldo inicial, modifica'l directament des de fora assignant-li
# un nou valor (compte.saldo = 500), i torna'l a imprimir.

# CREEM LA CLASSE COMPTE BANCARI I LI PASSEM COM ATRIBUTS EL NOM DEL TITULAR
# I EL SEU SALDO. FIQUEM 0.0 COM A SALDO PER DEFECTE ENTRE EL PARÉNTESIS, AIXÍ
# NO T'OBLIGA A POSAR EL SALDO QUAN CREES L'OBJECTE, PERÒ PER DEFECTE SEMPRE
# TINDRÀ 0.0
class CompteBancari:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo

# CREEM UN COMPTE I LI PASSEM NOMÉS EL NOM DEL TITULAR JA QUE EL SALDO NO
# CAL PASSAR-LI GRÀCIES A FICAR 0.0 PER DEFECTE. IMRPIMIM EL SALDO
compte1 = CompteBancari("Ariadna Pagès")
print(f"Saldo inicial = {compte1.saldo}")

# LI CANVIEM EL VALOR AL SALDO, DE 0.0 A 500 I EL TORNEM A IMPRIMIR
compte1.saldo = 500
print(f"Saldo final = {compte1.saldo}")