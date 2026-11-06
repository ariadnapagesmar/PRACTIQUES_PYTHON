# Exercici 7: La classe Reserva

# Enunciat: Crea una classe Reserva que relacioni tres elements: un Vehicle,
# un Conductor i un període (per exemple, data_inici i data_fi). Afegeix un
# mètode a la classe que imprimeixi un resum clar de qui ha reservat quin
# cotxe i quan.

# CREEM LA CLASSE CONDUCTOR
class Conductor:
    def __init__(self, nom, carnet):
        self.nom = nom
        self.carnet = carnet

# CREEM LA CLASSE VEHICLE
class Vehicle:
    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula

# CREEM LA CLASSE RESERVA, I COM ATRIBUTS LI PASSEM UN OBJECTE VEHICLE I
# UN ALTRE OBJECTE CONDUCTOR
class Reserva:
    def __init__(self, vehicle, conductor, data_inici, data_fi):
        self.vehicle = vehicle
        self.conductor = conductor
        self.data_inici = data_inici
        self.data_fi = data_fi

    # CREEM UN MÈTODE QUE MOSTRI ELS DETALLS DE LA RESERVA
    def resum_reserva(self):
        print(f"Cotxe reservat: {self.vehicle.marca} --- {self.vehicle.matricula}"
              f"\nConductor: {self.conductor.nom} --- {self.conductor.carnet}"
              f"\nData: {self.data_inici} --- {self.data_fi}")

# CREEM UN OBJECTE DE CADA CLASSE
conductor = Conductor("Ariadna Pagès", "123456789")
vehicle = Vehicle("Ford", "123456ASD")
reserva = Reserva(vehicle, conductor, "01-11-2026", "05-11-2026")

# CRIDEM EL MÈTODE EN LA RESERVA
reserva.resum_reserva()