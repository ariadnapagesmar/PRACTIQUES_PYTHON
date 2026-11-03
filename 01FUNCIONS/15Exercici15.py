# 5. Gestionar el fitxer no trobat (Fàcil-Mitjà)

# Intenta fer un programa que llegeixi un fitxer anomenat secret.txt (que no existeix
# a la teva carpeta). Utilitza un bloc try-except amb l'excepció FileNotFoundError
# per capturar l'error i mostrar per pantalla un missatge personalitzat:
# "Vaja, el fitxer secret no existeix".


try:
    with open("secret.txt", "r") as arxiu:
        contingut = arxiu.read()
        print(contingut)
except FileNotFoundError:
    print("Vaja, el fitxer secret no existeix.")