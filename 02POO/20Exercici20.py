# Exercici 10: El Mini-Sistema de Reserves (L'estrena del projecte)

# Enunciat: Construeix un petit script integrat on tinguis:
# Una classe Vehicle.
# Una classe Usuari.
# Una classe GestorFlota que permeti afegir vehicles, registrar usuaris,
# i fer una reserva associant un usuari a un vehicle (canviant l'estat
# del cotxe a "Ocupat" automàticament quan es fa la reserva).

# CREEM LA CLASSE VEHICLE. PER DEFAULT TOTS ESTAN DISPONIBLES
class Vehicle:
    def __init__(self, matricula, model, estat = "Disponible"):
        self.matricula = matricula
        self.model = model
        self.estat = estat

# CREEM LA CLASSE USUARI
class Usuari:
    def __init__(self, nom, dni):
        self.nom = nom
        self.dni = dni

# CREEM LA CLASSE GESTORFLOTA. ELS SEUS ATRIBUTS SON LES LLISTES PER GUARDAR
# ELS VEHICLES, ELS USUARIS I LES RESERVES
class GestorFlota:
    def __init__(self):
        self.flota = []
        self.usuaris = []
        self.vehicles_llogats = {}

    # MÈTODE PER AFEGIR UN VEHICLE A LA LLISTA DE VEHICLES SI LA MATRÍCULA
    # ÉS CORRECTA I ESTÀ BÉ
    def afegir_vehicle(self, vehicle):
        if len(vehicle.matricula) == 7:
            self.flota.append(vehicle)
            print(f"El vehicle amb matrícula {vehicle.matricula} s'ha reservat amb èxit.")
        else:
            print("La matrícula del vehicle no és vàlida.")

    # MÈTODE PER AFEGIR UN USUARI A LA LLISTA D'USUARIS SI EL DNI ÉS VÀLID
    def afegir_usuari(self, usuari):
        if len(usuari.dni) == 9:
            self.usuaris.append(usuari)
            print(f"L'usuari amb DNI {usuari.dni} s'ha afegit amb èxit.")
        else:
            print("El DNI de l'usuari no és vàlid.")

    # MÈTODE PER GUARDAR LES RESERVES AGAFANT LA MATRÍCULA DEL COTXE I
    # EL DNI DE L'USUARI
    def reservar_vehicle(self, vehicle, usuari):
        if vehicle in self.flota and usuari in self.usuaris:
            vehicle.estat = "Ocupat"
            self.vehicles_llogats[vehicle.matricula] = usuari.dni
            print(f"El vehicle amb matrícula {vehicle.matricula} s'ha reservat a l'usuari amb DNI {usuari.dni} amb èxit.")
        else:
            print("No s'ha pogut fer la reserva. El DNI o la matrícula no son vàlids.")

# CREEM 2 VEHICLES, 2 USUARIS I UN GESTOR
vehicle1 = Vehicle("1234ASD", "Ford Fiesta")
vehicle2 = Vehicle("4321DSA", "Toyota Corolla")
usuari1 = Usuari("Ariadna Pagès", "39961875L")
usuari2 = Usuari("Juan Ramon Pampin", "34521233M")
gestor = GestorFlota()

# AFEGIM ELS VEHICLES A LA FLOTA I ELS MOSTREM
gestor.afegir_vehicle(vehicle1)
gestor.afegir_vehicle(vehicle2)
for vehicle in gestor.flota:
    print(f"{vehicle.matricula} --- {vehicle.model} --- {vehicle.estat}")

# AFEGIM ELS USUARIS A LA LLISTA D'USUARIS I ELS MOSTREM
gestor.afegir_usuari(usuari1)
gestor.afegir_usuari(usuari2)
for usuari in gestor.usuaris:
    print(f"{usuari.nom} --- {usuari.dni}")

# FEM DOS RESERVES AMB ELS DOS VEHICLES I ELS DOS USUARIS I HO MOSTREM
gestor.reservar_vehicle(vehicle1, usuari1)
gestor.reservar_vehicle(vehicle2, usuari2)
for vehicle, usuari in gestor.vehicles_llogats.items():
    print(f"{vehicle} --- {usuari}")

# COMPROVEM QUE ELS COTXES HAGIN CANVIAT DE 'DISPONIBLE' A 'OCUPAT'
for vehicle in gestor.flota:
    print(f"{vehicle.matricula} --- {vehicle.model} --- {vehicle.estat}")
