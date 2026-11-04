# Exercici 4: Mètodes amb operacions (Ingressos i Extreccions)

# Objectiu: Modificar atributs de manera segura mitjançant mètodes.
# Enunciat: Millora la classe CompteBancari de l'exercici anterior. Afegeix-li
# dos mètodes:
# ingressar(quantitat): Suma la quantitat al saldo actual.
# retirar(quantitat): Resta la quantitat al saldo (assegura't amb un if que
# hi ha prou diners; si no n'hi ha, mostra un missatge d'error).

class CompteBancari:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo

compte1 = CompteBancari("Ariadna Pagès")
print(f"Saldo inicial = {compte1.saldo}")

compte1.saldo = 500
print(f"Saldo final = {compte1.saldo}")