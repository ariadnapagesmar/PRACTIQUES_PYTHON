# Exercici 2: Afegint un mètode simple

# Objectiu: Crear mètodes que facin servir els atributs de l'objecte.
# Enunciat: Reprèn la classe Cotxe de l'exercici anterior i afegeix-li un
# mètode anomenat descriure() que no rebi cap altre paràmetres excepte self.
# Aquest mètode ha de retornar (amb un return) una frase tipus: "Aquest
# cotxe és un [marca] [model] de l'any [any]". Crida el mètode des
# dels teus objectes.

# CREEM LA CLASSE COTXE I EL SEU CONSTRUCTOR UN ALTRE COM EXACTAMENT COM ABANS
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    # LI FEM UN MÈTODE AL COTXE QUE DONI AUTOMÀTICAMENT TOTA LA INFORMACIÓ
    def descriure(self):
        descripcio = f"Aquest cotxe és un {self.marca} {self.model} de l'any {self.any}."
        return descripcio

# CREEM ELS DOS COTXES
cotxe1 = Cotxe("Ford", "Fiesta", 2012)
cotxe2 = Cotxe("Seat", "Ibiza", 2010)

# IMRPIMIM LES DESCRIPCIONS DELS DOS COTXES
print(cotxe1.descriure())
print(cotxe2.descriure())