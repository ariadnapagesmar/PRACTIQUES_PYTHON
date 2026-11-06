# Exercici 1: Atributs privats i Getters/Setters manuals

# Enunciat: Crea una classe Vehicle amb un atribut privat __quilometratge
# (recorda que a Python es fa amb doble guió baix). Implementa dos mètodes:
# obtenir_quilometratge() (getter) i actualitzar_quilometratge(km) (setter).
# El setter ha de comprovar amb un if que els quilòmetres nous no siguin
# inferiors als actuals; si ho són, ha de mostrar un avís.

# CREEM LA CLASSE VEHICLE I LI AFEGIM L'ATRIBUT PRIVAT QUILOMETRATGE
class Vehicle:
    def __init__(self, model, quilometratge):
        self.model = model
        self.__quilometratge = quilometratge

    # CREEM EL GETTER AMB EL @PROPERTY PER PODER LLEGIR LA VARIABLE
    # COM SI FOS UNA NORMAL
    @property
    def quilometratge(self):
        return self.__quilometratge

    # CREEM EL SETTER AMB EL @QUILOMETRATGE.SETTER QUE TAMBÉ FA QUE
    # PUGUEM MODIFICAR LA VARIABLE COM SI FOS UNA NORMAL
    @quilometratge.setter
    def quilometratge(self, nous_km):
        # SI ELS NOUS KM SON MAJORS ALS ACTUALS, S'ACTUALITZA SENSE CAP
        # PROBLEMA. PERO SI HA INTRODUIT MENYS KM, AVISA QUE HI HA UN
        # ERROR I NO HO ACTUALITZA
        if nous_km >= self.__quilometratge:
            self.__quilometratge = nous_km
            print(f"Quilometratge actualitzat a {self.__quilometratge} km amb èxit.")
        else:
            print("Error. No pots tirar enrere el comptador de quilòmetres.")

# CREEM UN COTXE PER PROVAR EL GETTER I EL SETTER
cotxe = Vehicle("Ford Fiesta", 5000)

# PODEM IMPRIMIR EL QUILOMETRATGE SENSE CAP PROBLEMA COM SI FOS UNA VARIABLE NORMAL
print(cotxe.quilometratge)

# TAMBÉ LA PODEM MODIFICAR SENSE CAP PROBLEMA, SI FIQUEM UN KM IGUAL O MAJOR
cotxe.quilometratge = 10000
# SI EL FIQUEM MÉS PETIT, SALTA EL MISSATGE D'ERROR
cotxe.quilometratge = 1000