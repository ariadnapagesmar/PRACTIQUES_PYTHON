# Exercici 7: Cercar dins d'una llista d'objectes

# Objectiu: Filtrar objectes segons una condició.
# Enunciat: Partint de la llista flota de l'exercici anterior, escriu una
# funció externa (o un mètode) que rebi la llista i una matrícula. La funció
# ha de buscar a la llista el cotxe que coincideixi amb aquesta matrícula i
# retornar l'objecte cotxe (o un missatge si no existeix).

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

# CREEM LA FUNCIÓ A LA QUE LI PASSAREM LA LLISTA I UNA MATRÍCULA I BUSCAREM
# SI ALGUN COTXE DINS DE LA LLISTA TE LA MATRÍCULA QUE LI HEM PASSAT
def buscar_cotxe(llista, matricula):
    # CREEM UN COMPTADOR QUE SUMI U CADA COP QUE EL BUCLE FOR CANVII DE COTXE
    comptador = 0
    for cotxe in llista:
        # SI TROBEM EL COTXE EN QUESTIÓ. L'IMPRIMIM. SINO, SUMEM 1 AL COMPTADOR
        if cotxe.matricula == matricula:
            print(f"{cotxe.matricula} - {cotxe.model} - {cotxe.estat}")
        else:
            comptador += 1
    # FEM UN ALTRE IF FORA PER SI NO HI HA CAP COTXE AMB LA MATEIXA MATRÍCULA
    # SI EL COMPTADOR ARRIBA AL MATEIX NÚMERO QUE EL LENGTH DE LA LLISTA
    # SALTARÀ EL MISSATGE DE QUE NO ESTÀ EL COTXE
    if comptador == len(llista):
        print(f"No hem trobat cap cotxe amb la matrícula: {matricula}")

# CRIDEM LA FUNCIÓ. LI PASSEM LA LLISTA I UNA MATRÍCULA
buscar_cotxe(flota, "123457ASD")