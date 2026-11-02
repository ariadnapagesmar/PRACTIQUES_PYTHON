# 4. Docstrings i validació de contrasenyes (Mitjà)

# Crea una funció anomenada valida_contrasenya(contrasenya) que tingui un
# docstring professional descrivint què fa. La funció ha de retornar True
# si la contrasenya té una longitud (len()) de més de 8 caràcters i conté
# almenys una majúscula (podeu usar .upper()), o False en cas contrari. Posa
# a prova la funció amb diferents paraules.

# CREEM LA FUNCIÓ valida_contrasenya I FIQUEM LA CONDICIÓ DE QUE LA CONTRASENYA
# HA DE SER MÉS LLARGA QUE 8 CARÀCTERS I QUE CONTÉ ALGUNA MAJÚSCULA (AIXÒ ES FA
# COMPARANT LA CONTRASENYA DE L'USUARI AMB LA MATEIXA PERO AMB UN .LOWER(),
# SI SÓN DIFERENTS, VOL DIR QUE LA CONTRASENYA DE L'USUARI SÍ TÉ ALGUNA MAJÚSCULA)
def valida_contrasenya(contrasenya):
    """
    Comprovem si la contrasenya és segura.

    param:
        contrasenya (String): La contrasenya que ha de validar.

    return:
        bool: True si és segura, False si no ho és.
    """
    if len(contrasenya) > 8 and contrasenya != contrasenya.lower():
        return True
    else:
        return False

# DEMANEM LA CONTRASENYA A L'USUARI I CRIDEM LA FUNCIÓ
contrasenya_usuari = input("Escriu la teva contrasenya per veure si és "
                    "segura (True) o no ho és (False): ")
print(valida_contrasenya(contrasenya_usuari))