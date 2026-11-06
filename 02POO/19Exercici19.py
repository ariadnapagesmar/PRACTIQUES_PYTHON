# Exercici 9: Gestor de Flota amb filtres avançats

# Enunciat: Amplia el teu GestorFlota de l'exercici anterior perquè tingui
# un mètode anomenat obtenir_disponibles(). Aquest mètode ha de recórrer
# la llista de vehicles i retornar una nova llista exclusivament amb els
# cotxes que tinguin l'estat "Disponible".

# CREEM LA CLASSE VEHICLE
class Vehicle:
    def __init__(self, marca, matricula, estat):
        self.marca = marca
        self.matricula = matricula
        self.estat = estat

# CREEM LA CLASSE GESTOR DE VEHICLES. NOMÉS TINDRÀ D'ATRIBUT EL VEHICLE QUE
# VOLEM GESTIONAR, QUE PER DEFECTE NO SERÀ CAP
class GestorVehicles:
    def __init__(self):
        self.flota = []

    # CREEM UN MÈTODE QUE DONI D'ALTA EL VEHICLE (S'AFEGEIX A LA LLISTA)
    # SI LA MATRÍCULA TÉ 9 CARÀCTERS
    def alta_cotxe(self, vehicle):
        if len(vehicle.matricula) == 9:
            self.flota.append(vehicle)
            print(f"El cotxe amb matrícula {vehicle.matricula} s'ha donat d'alta amb èxit.")
        else:
            print("Matrícula invàlida.")

    # CREEM UN ALTRE MÈTODE QUE RECORRI LA LLISTA DE LA FLOTA I CREI UNA NOVA
    # LLISTA NOMÉS AMB ELS VEHICLES AMB ESTAT = DISPONIBLE
    def obtenir_disponibles(self):
        vehicles_disponibles = [vehicle for vehicle in self.flota
                               if vehicle.estat == "Disponible"]
        return vehicles_disponibles

# CREEM DIFERENTS VEHICLES I EL GESTOR
vehicle1 = Vehicle("Ford", "123456ASD", "Ocupat")
vehicle2 = Vehicle("Peugeot", "654321DSA", "Disponible")
vehicle3 = Vehicle("Kia", "987654MXZ", "En taller")
vehicle4 = Vehicle("Mercedes", "369842POI", "Disponible")
gestor = GestorVehicles()

# ELS DONEM D'ALTA AMB EL GESTOR
gestor.alta_cotxe(vehicle1)
gestor.alta_cotxe(vehicle2)
gestor.alta_cotxe(vehicle3)
gestor.alta_cotxe(vehicle4)

# RECORREM LA NOVA LLISTA I LA MOSTREM
for vehicle in gestor.obtenir_disponibles():
    print(f"{vehicle.matricula} --- {vehicle.marca} --- {vehicle.estat}")