# 4. Llegir un fitxer existent (Fàcil)

# Crea un programa que obri el fitxer salutacio.txt que acabes de crear en mode
# lectura ("r"), llegeixi tot el seu contingut amb .read(), ho imprimeixi per
# pantalla, i tanqui el fitxer amb .close().

arxiu = open("salutacio.txt", "r")
contingut = arxiu.read()
print(contingut)
arxiu.close()