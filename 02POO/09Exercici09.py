# Exercici 9: POO + Excepcions

# Objectiu: Controlar errors personalitzats amb classes.
# Enunciat: Crea una classe Llibre amb titol i exemplars_disposables. Afegeix un
# mètode prestar(). Si exemplars_disposables arriba a 0, el mètode ha de llançar
# una excepció pròpia (raise ValueError("No queden exemplars disponibles")).
# Després, utilitza un bloc try...except per capturar l'error quan intentis
# prestar un llibre esgotat.

# CREEM LA CLASSE LLIBRE I EL SEU CONSTRUCTOR
class Llibre:
    def __init__(self, titol, exemplars_disponibles):
        self.titol = titol
        self.exemplars_disponibles = exemplars_disponibles

    # CREEM LA FUNCIÓ PER PRESTAR LLIBRES. FEM UNA CONDICIÓ QUE SI ELS
    # EXEMPLARS_DISPONIBLES ARRIBEN A 0, LLANCEM UNA EXCEPCIÓ ValueError
    # FENT US DEL RAISE
    def prestar(self):
        if self.exemplars_disponibles < 1:
            raise ValueError("No queden exemplars disponibles d'aquest llibre.")

        # SI HI HA LLIBRES SUFICIENTS, ES RESTA UN
        self.exemplars_disponibles -= 1
        print(f"Has agafat prestat el llibre: {self.titol}")

# CREEM UN LLIBRE
llibre = Llibre("El principito", 0)

# PROVEM SI ES POT PRESTAR EL LLIBRE QUE ACABEM DE CREAR. SI NO ES POT PERQUE
# NO N'HI HA PROUS, ENS LLENÇA L'EXCEPCIÓ
try:
    llibre.prestar()
except ValueError as e:
    print(e)


