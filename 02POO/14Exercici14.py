# Exercici 4: Mètodes específics a les classes filles

# Enunciat: A partir de l'exercici anterior, afegeix un mètode general
# detalls() a la classe pare Vehicle. Després, sobreescriu (override)
# aquest mètode a les classes Cotxe i Furgoneta perquè mostrin la informació
# pròpia de cadascuna sumada a la del pare.

# CREEM LA CLASSE VEHICLE COMPLETAMENT NORMAL
class Vehicle:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca

    # I LI AFEGIM UNA FUNCIÓ QUE MOSTRI ELS DETALLS DELS ATRIBUTS
    def detalls(self):
        print(f"{self.matricula} --- {self.marca}")

# CREEM LA CLASSE COTXE QUE ES FILLA DE LA CLASSE VEHICLE, PER TANT FEM SERVIR
# super() I LI AFEGIM UN ATRIBUT PROPI
class Cotxe(Vehicle):
    def __init__(self, matricula, marca, num_portes):
        super().__init__(matricula, marca)
        self.num_portes = num_portes

    # FEM OVERRIDE (SOBREESCRIURE) LA FUNCIÓ DE VEHICLE PERQUE MOSTRI TOTES LES
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

# PER PROVAR-HO, CREEM UN OBJECTE DE CADA CLASSE
vehicle = Vehicle("123456MPO", "Mazda")
cotxe = Cotxe("654321GGH", "Ford", 5)
furgoneta = Furgoneta("678943ERT", "Kia", 350)

# I IMPRIMIM ELS DETALLS DE LES TRES PER COMPROBAR QUE LA FUNCIÓ detalls()
# FUNCIONA SENSE CAP PROBLEMA
vehicle.detalls()
cotxe.detalls()
furgoneta.detalls()