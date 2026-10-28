# 6. Preus amb Tuples i Desglossament

# Concepte: Tuples, llistes de tuples, bucle for.

# Enunciat: Imagina que tens una llista de productes on cada element és una tupla
# amb el nom del producte i el seu preu: botiga = [("poma", 1.20), ("llet", 0.95),
# "pa", 0.80) -> (ignora aquesta, fes-ho bé: ("pa", 0.80)), ("formatge", 3.50)].

# Recorre la llista amb un bucle for, desglossant cada tupla en producte i preu.

# Imprimeix cada element amb un f-string amb el format:
# Producte: [nom] - Preu: [preu] €.

# Opcional: Calcula el preu total de tots els productes sumats.

botiga = [("poma", 1.20), ("llet", 0.95), ("pa", 0.80), ("formatge", 3.50)]

preu_total = 0

for producte in botiga:
    print(f"Producte: {producte[0]} - Preu: {producte[1]}")
    preu_total += producte[1]

print(f"Preu total: {preu_total}")

# MANERA MÉS NETA DE FER-HO: FICAR DOS NOMS DE VARIABLES EN EL BUCLE EN COMPTES DE
# FER SERVIR ELS INDEX[0, 1]

botiga1 = [("poma", 1.20), ("llet", 0.95), ("pa", 0.80), ("formatge", 3.50)]

preu_total1 = 0

# En lloc de dir 'for producte in botiga:', assignem directament un nom per a cada part de la tupla:
for nom, preu in botiga1:
    print(f"Producte: {nom} - Preu: {preu}")
    preu_total1 += preu

print(f"Preu total: {preu_total1}")