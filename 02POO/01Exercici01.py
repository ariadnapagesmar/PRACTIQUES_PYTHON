# Exercici 1: El teu primer objecte (Cotxe bàsic)

# Objectiu: Crear una classe bàsica i instanciar objectes.
# Enunciat: Crea una classe anomenada Cotxe. El seu mètode constructor __init__
# ha de rebre tres paràmetres: marca, model i any. Després, crea dos objectes
# diferents d'aquesta classe (dos cotxes reals) i imprimeix per pantalla
# les seves dades.

# CREEM LA CLASSE 'COTXE' I EL SEU CONSTRUCTOR, AMB ELS ATRIBUTS: LA MARCA,
# EL MODEL I L'ANY DEL COTXE
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

# CREEM DOS COTXES I LI PASSEM ELS ARGUMENTS AL CONSTRUCTOR ENTRE PARÉNTESIS
cotxe1 = Cotxe("Ford", "Fiesta", 2012)
cotxe2 = Cotxe("Seat", "Ibiza", 2010)

# IMRPIMIM LA INFORMACIÓ DELS DOS OBJECTES
print("Cotxe 1:\n"
      f"Marca --- {cotxe1.marca}\n"
      f"Model --- {cotxe1.model}\n"
      f"Any --- {cotxe1.any}\n"
      "Cotxe 2:\n"
      f"Marca --- {cotxe2.marca}\n"
      f"Model --- {cotxe2.model}\n"
      f"Any --- {cotxe2.any}")

