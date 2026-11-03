# 3. Escriure el teu primer fitxer (Fàcil)

# Crea un programa que obri un fitxer anomenat salutacio.txt en mode escriptura ("w").
# Fes que escrigui a dins la frase "Hola! Aquest és el meu primer fitxer des de Python."
# i tanca el fitxer correctament amb .close(). Comprova a la teva carpeta de PyCharm
# que el fitxer s'ha creat.

arxiu = open("salutacio.txt", "w")
arxiu.write("Hola! Aquest és el meu primer fitxer des de Python.")
arxiu.close()