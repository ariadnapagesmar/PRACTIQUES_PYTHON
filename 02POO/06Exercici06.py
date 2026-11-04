# Exercici 6: Llistes d'objectes

# Objectiu: Guardar i recórrer objectes dins d'una llista de Python.
# Enunciat: Crea tres objectes diferents de la classe VehicleEmpresa de
# l'exercici anterior. Guarda aquests tres objectes dins d'una llista
# anomenada flota. Fes un bucle for que recorri la llista flota i
# imprimeixi la matrícula i l'estat de cada cotxe.

# CREEM LA CLASE VEHICLEEMPRESA I CREEM EL SEU CONSTRUCTOR
class VehicleEmpresa:
    def __init__(self, matricula, model, estat):
        self.matricula = matricula
        self.model = model
        self.estat = estat

# CREEM TRES COTXES DIFERENTS
cotxe1 = VehicleEmpresa("123456ASD", "Ford Fiesta", "Disponible")
cotxe2 = VehicleEmpresa("654321MBN", "Seat Ibiza", "Ocupat")
cotxe3 = VehicleEmpresa("987123KJL", "Toyota Corolla", "En taller")

# I ELS GUARDEM EN UNA LLISTA
flota = [cotxe1, cotxe2, cotxe3]

# FEM UN BUCLE FOR DINS DE LA LLISTA E IMPRIMIM LA MATRÍCULA I L'ESTAT DE CADA COTXE
for cotxe in flota:
    print(f"{cotxe.matricula} - {cotxe.estat}")




