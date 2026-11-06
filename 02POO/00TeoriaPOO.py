# PROGRAMACIÓ ORIENTADA A OBJECTES (POO)

# Què és una classe i un objecte?
# Fins ara has utilitzat funcions i variables soltes. La Programació Orientada a
# Objectes (POO) serveix per agrupar les dades i les accions lògiques en "paquets"
# anomenats classes.
#
# - Una classe és com un "plànol" o un "molde" (per exemple, el plànol d'un cotxe).
# - Un objecte és la instància d'aquesta classe, és a dir, un cotxe real i concret
#   construït a partir d'aquell plànol.


# Definir una classe bàsica i crear objectes

# Per definir una classe fem servir la paraula clau 'class' seguida del nom
# (per convenció a Python, s'escriu amb la primera lletra en majúscula).

class Cotxe:
    pass  # La paraula 'pass' s'utilitza quan la classe està buida temporalment

# Per crear un objecte (instanciar la classe), escrivim el nom de la classe amb parèntesis:
cotxe_meu = Cotxe()
cotxe_teu = Cotxe()

print(type(cotxe_meu))  # Imprimeix <class '__main__.Cotxe'>


# El mètode constructor (__init__) i el paràmetre 'self'

# Quan creem un cotxe real, volem que tingui propietats úniques (atributs), com la
# marca, el model o la matrícula. Per fer això, fem servir un mètode especial
# anomenat constructor (__init__), que s'executa automàticament en crear l'objecte.
#
# El paràmetre 'self' fa referència a l'objecte concret que s'està creant en aquell moment.

class Vehicle:
    def __init__(self, marca, model, matricula):
        self.marca = marca          # Atribut de l'objecte
        self.model = model          # Atribut de l'objecte
        self.matricula = matricula  # Atribut de l'objecte
        self.estat = "Disponible"   # Atribut amb un valor fix per defecte

# Creem objectes (vehicles reals) passant-li els arguments al constructor:
vehcle1 = Vehicle("Toyota", "Corolla", "1234-ABC")
vehcle2 = Vehicle("Seat", "Ibiza", "5678-XYZ")

print(vehcle1.marca)      # Imprimeix "Toyota"
print(vehcle2.matricula)  # Imprimeix "5678-XYZ"
print(vehcle1.estat)      # Imprimeix "Disponible"


# Valors per defecte als paràmetres del constructor (__init__)

# Pots posar un valor per defecte directament a la definició del mètode. Si ho fas
# així després el constructor no t'obliga a definir tu mateix el valor de
# l'atribut en qüestió.

# Opció A: Si ho fas així (Sense valor per defecte)
class CompteBancari:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  # T'obliga a passar-li un saldo sí o sí
# Si intentessis fer això, et donaria error (TypeError falta un argument):
# compte1 = CompteBancari("Anna")
# Aquí et demanaria obligatòriament posar un número cada vegada: compte1 = CompteBancari("Anna", 0.0).

# Opció B: Amb valor per defecte (El que demana l'exercici 3)
# Perquè puguis crear el compte posant només el titular (o el nom), pots assignar
# un valor directament al paràmetre del constructor posant un = al costat:
class CompteBancari:
    # Posem saldo = 0.0 com a valor per defecte
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo  # Agafarà 0.0 si no li dius res més
# Ara pots crear el compte de dues maneres totalment vàlides:
# 1. Només amb el titular (agafarà 0.0 automàticament):
compte_anna = CompteBancari("Anna")
print(compte_anna.saldo)  # Imprimeix: 0.0
# 2. O passant-li directament un saldo inicial si ja té diners:
compte_pere = CompteBancari("Pere", 150.50)
print(compte_pere.saldo)  # Imprimeix: 150.50


# Mètodes (Funcions dins de les classes)

# Els mètodes són funcions que viuen dins d'una classe i defineixen el comportament
# o les accions que pot fer un objecte. Igual que __init__, sempre han de portar
# 'self' com a primer paràmetre per poder accedir als atributs de l'objecte.

class VehicleAmbMetodes:
    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula
        self.estat = "Disponible"

    # Mètode per llogar el vehicle
    def llogar(self):
        if self.estat == "Disponible":
            self.estat = "En ruta / Ocupat"
            print(f"El vehicle {self.matricula} ha estat llogat correctament.")
        else:
            print(f"Error: El vehicle {self.matricula} ja està ocupat!")

    # Mètode per retornar el vehicle
    def retornar(self):
        self.estat = "Disponible"
        print(f"El vehicle {self.matricula} ha estat retornat a l'empresa.")

# Utilitzem la classe i executem els seus mètodes:
cotxe_empresa = VehicleAmbMetodes("Renault", "9999-ZZZ")

print(cotxe_empresa.estat)  # Imprimeix "Disponible"
cotxe_empresa.llogar()      # Canvia l'estat a "En ruta / Ocupat"
print(cotxe_empresa.estat)  # Imprimeix "En ruta / Ocupat"

cotxe_empresa.retornar()    # Torna a posar l'estat a "Disponible"


# ENCAPSULAMENT --- GETTERS I SETTERS

# Imagina que tens un atribut important en un objecte (com el saldo d'un compte o
# els quilòmetres d'un cotxe) i no vols que ningú el pugui modificar des de fora
# posant una barbaritat (per exemple, un saldo negatiu o uns quilòmetres impossibles).

# Encapsular: Significa "amagar" l'atribut real posant-li un doble guió baix davant
# (self.__atribut). Així evitem que des de fora es pugui fer
# cotxe.__quilometratge = -5000 directament.
# Getter: És el mètode que serveix per llegir (get) el valor d'aquell atribut privat
# de manera segura.
# Setter: És el mètode que serveix per modificar (set) el valor d'aquell atribut, però
# posant-hi condicions o filtres (un if) per validar que el nou valor té sentit.

# A Python hi ha una manera molt elegant i neta de fer això sense haver de crear
# funcions amb noms llargs com obtenir_... o actualitzar_.... S'utilitzen els decoradors
# @property i @nom_atribut.setter.
# Permet que l'atribut sembli públic a la vista de qui l'utilitza, però per sota passa
# pel filtre del setter automàticament!

class CotxeModern:
    def __init__(self, model, quilometratge_inicial):
        self.model = model
        self.__quilometratge = quilometratge_inicial  # Atribut privat

    # --- GETTER EN FORMAT PYTHONIC (@property) ---
    # Fa que puguem llegir l'atribut privat com si fos una variable normal
    @property
    def quilometratge(self):
        return self.__quilometratge

    # --- SETTER EN FORMAT PYTHONIC (@quilometratge.setter) ---
    # S'executa automàticament cada cop que fem: cotxe.quilometratge = valor
    @quilometratge.setter
    def quilometratge(self, nous_km):
        if nous_km >= self.__quilometratge:
            self.__quilometratge = nous_km
            print(f"Quilometratge actualitzat a {self.__quilometratge} km.")
        else:
            print("Error: No pots tirar enrere el comptador de quilòmetres!")


# --- PROVEM LA CLASSE MODERNA ---
cotxe2 = CotxeModern("Tesla Model 3", 5000)

# 1. Per LLEGIR el valor, sembla que accedim a una propietat normal (gràcies al @property):
print(cotxe2.quilometratge)  # Imprimeix: 5000 (crida al getter automàticament)

# 2. Per MODIFICAR el valor, fem una assignació normal,
# però per sota s'activa el setter i valida la condició del if:
cotxe2.quilometratge = 5200   # Funciona i actualitza!

cotxe2.quilometratge = 3000   # Dispara el missatge d'error del setter!


# HERENCIA

# Imagina que tens una classe general (la classe pare o superclasse) amb
# atributs i mètodes comuns, com per exemple Vehicle. En lloc de tornar a
# escriure tot allò per a un Cotxe o una Furgoneta, fas que aquestes noves
# classes (classes filles o subclasses) "heretin" directament tot el que
# té el pare, i només afegeixis o modifiquis allò que tenen d'específic.

# La sintaxi a Python (Amb exemples i comentaris)
# Per fer que una classe filla hereti d'una classe pare, simplement posem
# el nom del pare entre parèntesis al costat de la classe filla:
# class Filla(Pare):.

# 1. CLASSE PARE (Superclasse)
# Té els atributs i mètodes generals que qualsevol vehicle compartirà.
class Vehicle:
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.estat = "Disponible"

    def descriure(self):
        return f"Vehicle {self.marca} amb matrícula {self.matricula}"

# 2. CLASSE FILLA (Subclasse)
# Posem (Vehicle) entre parèntesis per indicar que 'Cotxe' hereta de 'Vehicle'.
class Cotxe(Vehicle):
    def __init__(self, matricula, marca, num_portes):
        # super() serveix per cridar el constructor de la classe pare (Vehicle)
        # i així no hem de tornar a escriure self.matricula i self.marca a mà.
        super().__init__(matricula, marca)

        # Ara afegim l'atribut nou i exclusiu d'un cotxe
        self.num_portes = num_portes

    # Podem crear mètodes exclusius només per als cotxes
    def obrir_maleter(self):
        print(f"El maleter del cotxe {self.matricula} està obert.")


# 3. UNA ALTRA CLASSE FILLA PER VEURE LA DIFERÈNCIA
class Furgoneta(Vehicle):
    def __init__(self, matricula, marca, capacitat_kg):
        super().__init__(matricula, marca)  # Heretem del pare
        self.capacitat_kg = capacitat_kg  # Atribut propi de la furgoneta

# --- PROVEM LA HERÈNCIA ---

# Creem un objecte de la classe filla 'Cotxe'
cotxe1 = Cotxe("1234-ABC", "Seat", 5)

# Fíxat: El cotxe pot utilitzar mètodes de la classe pare (Vehicle)
# tot i que no els haguem escrit a la classe Cotxe!
print(cotxe1.descriure())  # Imprimeix: Vehicle Seat amb matrícula 1234-ABC

# I també pot utilitzar els seus propis mètodes exclusius:
cotxe1.obrir_maleter()  # Imprimeix: El maleter del cotxe 1234-ABC està obert.

# I té accés als seus atributs propis:
print(f"Portes: {cotxe1.num_portes}")  # Imprimeix: Portes: 5