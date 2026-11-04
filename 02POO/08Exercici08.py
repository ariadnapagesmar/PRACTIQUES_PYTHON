# Exercici 8: Relació entre classes (Cotxe i Conductor)

# Objectiu: Fer que un objecte contingui un altre objecte.
# Enunciat: Crea una classe Conductor amb atributs nom i carnet. Després,
# modifica la classe VehicleEmpresa perquè tingui un atribut anomenat
# conductor_actual, que inicialment sigui None (cap conductor). Afegeix
# un mètode assignar_conductor(conductor) que guardi l'objecte conductor
# dins del vehicle quan algú se l'emporti.

# LA CLASSE CONDUCTOR I EL SEU CONSTRUCTOR
class Conductor:
    def __init__(self, nom, carnet):
        self.nom = nom
        self.carnet = carnet

# LA CLASSE VEHICLEEMPRESA I EL SEU CONSTRUCTOR. PER DEFECTE FIQUEM QUE
# NO HI HA CAP CONDUCTOR ACTUAL
class VehicleEmpresa:
    def __init__(self, matricula, model, estat, conductor_actual = None):
        self.matricula = matricula
        self.model = model
        self.estat = estat
        self.conductor_actual = conductor_actual

    # LI CREEM UN MÈTODE A AQUESTA CLASSE QUE SERVEIXI PER ASSIGNAR
    # UN CONDUCTOR (DE LA CLASSE CONDUCTOR) AL VEHICLE
    def assignar_conductor(self, conductor):
        self.conductor_actual = conductor

# CREEM UN CONDUCTOR I UN COTXE
conductor = Conductor("Ariadna Pagès", "32156765")
cotxe = VehicleEmpresa("123456ASD", "Ford Fiesta", "Ocupat")

# CRIDEM EL MÈTODE I LI ASSIGNEM UN CONDUCTOR AL VEHICLE
cotxe.assignar_conductor(conductor)
# HO MOSTREM PER LA CONSOLA
print(f"{cotxe.matricula} - {cotxe.model} - {cotxe.estat} - "
      f"{cotxe.conductor_actual.nom}")