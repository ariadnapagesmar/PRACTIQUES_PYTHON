# Exercici 6: La classe Conductor i la classe Vehicle

# Enunciat: Crea una classe Conductor amb atributs nom i carnet. Després,
# modifica la classe Vehicle perquè tingui un atribut conductor_assignat que
# inicialment sigui None. Afegeix un mètode assignar_conductor(conductor) i
# un altre alliberar_vehicle().

# CREEM LA CLASSE CONDUCTOR
class Conductor:
    def __init__(self, nom, carnet):
        self.nom = nom
        self.carnet = carnet

# CREEM A CLASSE VEHICLE. AFEGIM L'ATRIBUT conductor_assignat I FEM QUE
# SIGUI None PER DEFAULT
class Vehicle:
    def __init__(self, matricula, marca, conductor_assignat = None):
        self.matricula = matricula
        self.marca = marca
        self.conductor_assignat = conductor_assignat

    # CREEM EL MÈTODE PER ASSIGNAR UN CONDUCTOR AL VEHICLE. NOMÉS CAL CANVIAR
    # conductor_assignat DE None AL CONDUCTOR QUE PASSEM PER PARÀMETRE
    def assignar_conductor(self, conductor):
        self.conductor_assignat = conductor

    # CREEM EL MÈTODE PER TORNAR A TINDRE EL VEHICLE SENSE CONDUCTOR
    def alliberar_vehicle(self):
        self.conductor_assignat = None

    # FEM UN MÈTODE QUE MOSTRI ELS DETALLS DEL VEHICLE. AIXÍ PODREM VEURE SI TÉ
    # CONDUCTOR ASSIGNAT O NO
    def detalls(self):
        if self.conductor_assignat is not None:
            print(f"{self.matricula} --- {self.marca} --- {self.conductor_assignat.nom}")
        else:
            print(f"{self.matricula} --- {self.marca} --- Sense conductor")

# CREEM UN VEHICLE I UN CONDUCTOR
conductor = Conductor("Ariadna Pagès", "98887666KS")
vehicle = Vehicle("1234546ASD", "Ford")

# MOSTREM ELS DETALLS DEL VEHICLE QUE HEM CREAT
vehicle.detalls()

# LI ASSIGNEM EL CONDUCTOR QUE HEM CREAT
vehicle.assignar_conductor(conductor)

# MOSTREM ELS DETALLS UN ALTRE COP
vehicle.detalls()

# LI TREIEM EL CONDUCTOR ASSIGNAT AL VEHICLE
vehicle.alliberar_vehicle()

# MOSTREM ELS DETALLS UN ÚLTIM COP
vehicle.detalls()