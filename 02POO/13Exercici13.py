# Exercici 3: Herència bàsica de Vehicles

# Enunciat: Construeix una classe pare anomenada Vehicle amb atributs matricula
# i marca. Després, crea dues classes filles: Cotxe (que afegeixi l'atribut
# num_portes) i Furgoneta (que afegeixi l'atribut capacitat_carrega_kg).
# Fes servir super() per inicialitzar els atributs del pare.

class Vehicle:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca

class Cotxe(Vehicle):
    def __init__(self, matricula, marca, num_portes):
        super().__init__(matricula, marca)
        self.num_portes = num_portes

class Furgoneta(Vehicle):
    def __init__(self, matricula, marca, capacitat_carrega_kg):
        super().__init__(matricula, marca)
        self.capacitat_carrega_kg = capacitat_carrega_kg

