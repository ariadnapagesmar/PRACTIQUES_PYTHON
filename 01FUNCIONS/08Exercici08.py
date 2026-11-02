# 8. Comptador de vocals avançat amb Scope Global/Local (Avançat)

# Declara una variable global anomenada vocals_totals = 0. Després, crea una
# funció anomenada compta_vocals(text) que tingui variables locals per comptar
# les 'a', 'e', 'i', 'o', 'u' d'un text rebut per paràmetre. La funció ha de
# retornar quantes vocals té aquella paraula concreta, i a més, ha d'actualitzar
# (fent servir la paraula clau global) la variable global vocals_totals
# acumulant totes les vocals de totes les paraules que s'hagin analitzat al
# llarg del programa.

# DECLAREM LA VARIABLE ON ES GUARDARAN EL TOTAL DE TOTES LES VOCALS CONTADES
# EN TOT EL PROGRAMA I LI FIQUEM DE VALOR 0
vocals_totals = 0

# CREEM LA FUNCIÓ. CRIDEM LA VARIABLE vocals_totals AMB LA PARAULA 'global' PERQUÈ
# PYTHON ENTENGUI QUE NO VULL CREAR UNA NOVA VARIABLE, SINO FER SERVIR LA DE FORA
# I AIXÍ PODER SUMAR-LI DIRECTAMENT EL NOMBRE DE VOCALS EN EL TEXT
def compta_vocals(text):
    global vocals_totals
    text = text.lower()
    comptador = 0
    # FEM UN text.count("x") PER A QUE BUSQUI EL CARÀCTER PASSAT PER EL PARÀMETRE
    # I CONTI QUANTS COPS SURT. AIXÍ AMB LES 5 VOCALS
    comptador += text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
    vocals_totals += comptador
    return vocals_totals

compta_vocals("Hola caracola")
print(vocals_totals)
compta_vocals("Hola pepsicola")
print(vocals_totals)
compta_vocals("M'agrada molt Python")
print(vocals_totals)