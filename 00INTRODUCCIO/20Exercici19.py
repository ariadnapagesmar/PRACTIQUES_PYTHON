# 9. Intersecció d'aficions entre dos amics

# Concepte: Sets, operacions de conjunts (&), input(), bucles.

# Enunciat: Defineix dos conjunts amb les aficions de dues persones diferents:
# aficions_anna = {"fubol", "lectura", "cinema", "videojocs"}
# aficions_marc = {"cinema", "musica", "videojocs", "viatjar"}

# Utilitza les operacions de conjunts apreses als apunts per trobar quines
# aficions tenen en comú (intersecció).

# Fes que l'usuari pugui afegir una nova afició a l'Anna mitjançant input() i .add().
# Torna a calcular la intersecció i mostra el resultat actualitzat amb un f-string.

aficions_anna = {"fubol", "lectura", "cinema", "videojocs"}
aficions_marc = {"cinema", "musica", "videojocs", "viatjar"}

aficions_en_comu = aficions_anna & aficions_marc
print(aficions_en_comu)

aficions_anna.add(input("Afegeix un altre afició a l'Anna: ").lower())

aficions_en_comu = aficions_anna & aficions_marc
print(aficions_en_comu)