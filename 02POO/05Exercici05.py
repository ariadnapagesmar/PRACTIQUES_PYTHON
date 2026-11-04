# Exercici 5: Una classe per a la teva flota (Vehicle de pràctiques)

# Objectiu: Crear una classe amb estats lògics semblants al teu projecte.
# Enunciat: Crea una classe VehicleEmpresa amb els atributs matricula, model i
# estat (aquest últim comença sent "Disponible" per defecte). Afegeix un mètode
# canviar_estat(nou_estat) que permeti actualitzar l'estat del cotxe. Prova de
# crear un cotxe, canviar-lo a "En taller" i imprimir l'estat final.

# CREEM LA CLASSE I EL CONSTRUCTOR. FIQUEM COM A ESTAT PER DEFECTE 'DISPONIBLE'
class VehicleEmpresa:
    def __init__(self, matricula, model, estat = "Disponible"):
        self.matricula = matricula
        self.model = model
        self.estat = estat

    # CREEM EL MÈTODE QUE SERVEIX QUE CANVIAR L'ESTAT DEL COTXE
    def canviar_estat(self, nou_estat):
        self.estat = nou_estat.capitalize()

# CREEM UN COTXE, E IMPRIMIM L'ESTAT ACTUAL DEL COTXE
cotxe1 = VehicleEmpresa("456712GGD", "Golf")
print(cotxe1.estat)

# LI PASSEM AL COTXE EL MÈTODE PER CANVIAR EL SEU ESTAT, I L'IMPRIMIM
cotxe1.canviar_estat("En taller")
print(cotxe1.estat)