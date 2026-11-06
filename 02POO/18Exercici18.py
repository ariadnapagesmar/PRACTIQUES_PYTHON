# Exercici 8: Validació de Matrícules amb Excepcions Pròpies (raise)

# Enunciat: Crea una classe de gestió de vehicles. Quan s'intenti donar
# d'alta un cotxe, el mètode ha de comprovar si la matrícula compleix
# un format mínim (per exemple, que tingui una longitud determinada o
# contingui caràcters vàlids). Si no és així, fes un
# raise ValueError("Matrícula invàlida").

# CREO LA CLASSE VEHICLE
class Vehicle:
    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula

# CREO LA CLASSE GESTOR DE VEHICLES. NOMÉS TINDRÀ D'ATRIBUT EL VEHICLE QUE
# VOLEM GESTIONAR, QUE PER DEFECTE NO SERÀ CAP
class GestorVehicles:
    def __init__(self):
        self.flota = []

    # CREEM UN MÈTODE QUE DONI D'ALTA EL VEHICLE (SE LI ASSIGNI COM ATRIBUT
    # AL GESTOR) SI LA MATRÍCULA TÉ 9 CARÀCTERS. SINO, SALTA UN ValueError
    def alta_cotxe(self, vehicle):
        if len(vehicle.matricula) == 9:
           self.flota.append(vehicle)
           print("El cotxe s'ha donat d'alta amb èxit.")
        else:
            raise ValueError("Matrícula invàlida.")

# CREEM UN OBJECTE DE CADA
gestor = GestorVehicles()
vehicle = Vehicle("Ford", "123456ASD")

# PROVEM A AFEGIR EL VEHICLE AL GESTOR. SI LA MATRÍCULA ESTÀ BÉ HO FARÀ
# SINO SALTA L'ERROR DIRECTAMENT
try:
    gestor.alta_cotxe(vehicle)
except ValueError as e:
    print(e)