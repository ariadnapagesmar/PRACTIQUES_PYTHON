# Exercici 5: Polimorfisme amb una llista de vehicles mixtos

# Enunciat: Crea una llista flota_variada que contingui objectes de tipus Cotxe,
# Furgoneta i qualsevol altre vehicle. Fes un bucle for que recorri la llista
# i cridi al mètode detalls() de cada objecte, veient com cadascun respon a
# la seva manera tot i compartir la mateixa crida (polimorfisme pur).

# CREEM LA CLASSE VEHICLE COMPLETAMENT NORMAL
class Vehicle:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca

    # I LI AFEGIM UNA FUNCIÓ QUE MOSTRI ELS DETALLS DELS ATRIBUTS
    def detalls(self):
        print(f"{self.matricula} --- {self.marca}")

# CREEM LA CLASSE COTXE QUE ÉS FILLA DE LA CLASSE VEHICLE, PER TANT FEM SERVIR
# super() I LI AFEGIM UN ATRIBUT PROPI
class Cotxe(Vehicle):
    def __init__(self, matricula, marca, num_portes):
        super().__init__(matricula, marca)
        self.num_portes = num_portes

    # FEM OVERRIDE (SOBREESCRIURE) LA FUNCIÓ DE VEHICLE PERQUÈ MOSTRI TOTES LES
    # DADES DE COTXE TAMBÉ
    def detalls(self):
        print(f"{self.matricula} --- {self.marca} --- {self.num_portes} portes")

# FEM AMB FURGONETA EXACTAMENT EL MATEIX QUE HEM FET AMB COTXE
class Furgoneta(Vehicle):
    def __init__(self, matricula, marca, capacitat_carrega_kg):
        super().__init__(matricula, marca)
        self.capacitat_carrega_kg = capacitat_carrega_kg

    def detalls(self):
        print(f"{self.matricula} --- {self.marca} --- {self.capacitat_carrega_kg}kg de massa màxima")

# PER PROVAR-HO, CREEM DIFERENTS OBJECTES DE CADA CLASSE
vehicle1 = Vehicle("123456MPO", "Mazda")
vehicle2 = Vehicle("567890LDS", "Yamaha")
cotxe1 = Cotxe("654321GGH", "Ford", 5)
cotxe2 = Cotxe("347854TYF", "Peugeot", 3)
furgoneta1 = Furgoneta("678943ERT", "Kia", 350)
furgoneta2 = Furgoneta("912556WGM", "Citroen", 400)

# FEM LA LLISTA I ELS GUARDEM TOTS DINS
flota_variada = [vehicle1, vehicle2, cotxe1, cotxe2, furgoneta1, furgoneta2]

# FEM UN BUCLE FOR DINS DE LA LLISTA I MOSTREM ELS DETALLS DE CADA VEHICLE
for vehicle in flota_variada:
    vehicle.detalls()

