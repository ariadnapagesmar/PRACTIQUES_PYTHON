# 4. Filtrar paraules llargues (Llista per comprensió)

# Concepte: Llistes per comprensió, mètodes de string (.upper(), len()).

# Enunciat: Partint d'una llista de paraules:
# paraules = ["ordinador", "gat", "programacio", "gos", "python", "sol"].
# Utilitza una llista per comprensió per crear una nova llista que contingui
# només aquelles paraules que tinguin més de 4 lletres, i transforma-les totes
# a majúscules. Imprimeix el resultat.


paraules = ["ordinador", "gat", "programacio", "gos", "python", "sol"]

paraules_llargues = [x.upper() for x in paraules if len(x) > 4]

print(paraules_llargues)