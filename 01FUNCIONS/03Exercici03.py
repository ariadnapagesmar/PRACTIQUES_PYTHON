# 3. Funció Lambda de conversió de temperatura (Fàcil-Mitjà)

# Utilitzant una funció lambda, crea una funció anònima anomenada
# celsius_a_fahrenheit que transformi graus Celsius a Fahrenheit segons la
# fórmula: (Celsius * 9/5) + 32. Passa-li un parell de valors de prova (per exemple,
# 0 Celsius i 25 Celsius) i imprimeix els resultats mitjançant un f-string.

# DECLAREM LA FUNCIÓ LAMBDA, FENT EL CÀLCUL EN LA MATEIXA LÍNIA DE CODI
celsius_a_fahrenheit = lambda x: (x * 9 / 5) + 32

# LA CRIDEM DINS D'UN F-STRING
print(f"0.0 graus Celsius són {celsius_a_fahrenheit(0)} graus Fahrenheit.")
print(f"25.0 graus Celsius són {celsius_a_fahrenheit(25)} graus Fahrenheit.")