# Exercici 10: El Mini-CRUD Orientat a Objectes (El pont cap al teu projecte)

# Objectiu: Juntar tot en un petit programa de consola interactiu.
# Enunciat: Crea una classe anomenada GestorFlota. Aquesta classe
# ha de tenir internament una llista de vehicles. Implementa mètodes a la classe per:
# Afegir un nou vehicle a la llista.
# Llistar tots els vehicles de la flota.
# Canviar l'estat d'un vehicle buscant-lo per la seva matrícula.

class VehicleEmpresa:
    def __init__(self, matricula, model, estat):
        self.matricula = matricula
        self.model = model
        self.estat = estat

class GestorFlota:
    def __init__(self):
        self.flota = []

    def afegir_vehicle(self, vehicle):
        self.flota.append(vehicle)

    def llistar_vehicles(self):
        for vehicle in self.flota:
            print(f"{vehicle.matricula} - {vehicle.model} - {vehicle.estat}")

    def canviar_estat(self, matricula):
        trobat = False

        for vehicle in self.flota:
            if vehicle.matricula == matricula:
                estat = input(f"En quin estat està el vehicle amb matrícula: {vehicle.matricula}? ").capitalize()
                vehicle.estat = estat
                trobat = True
        if not trobat:
            print(f"No hi ha cap vehicle amb la matrícula: {matricula}")

cotxe = VehicleEmpresa("123456ASD", "Ford Fiesta", "Disponible")
gestor = GestorFlota()

gestor.afegir_vehicle(cotxe)
gestor.llistar_vehicles()

gestor.canviar_estat("123456ASD")
gestor.llistar_vehicles()