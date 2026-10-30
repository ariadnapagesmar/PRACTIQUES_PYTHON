# 9. Mini-Diccionari de traduccions interactiu (Diccionaris + Control d'errors)

# Crea un diccionari petit bilingüe (català-anglès) amb 5 paraules. Fes un bucle
# while continu on l'usuari pugui demanar la traducció d'una paraula. Si la
# paraula existeix al diccionari, mostra-la; si no existeix, pregunta a l'usuari
# si vol afegir-la demanant-li la seva traducció a l'anglès, actualitzant així el
# diccionari "al vol".

# CREEM UN DICCIONARI ON GUARDEM PARAULES EN CATALÀ I LA SEVA TRADUCCIÓ EN ANGLÈS
diccionari_bilingue = {
    "patates": "potatoes",
    "pernil": "ham",
    "cadira": "chair",
    "taula": "table",
    "pantalla": "screen"
}

# PREGUNTEM QUINA PARAULA VOL TRADUIR I LA GUARDEM
resposta_paraula = input("Quina paraula vols traduir? Escriu 'sortir' quan hagis acabat: ").lower()

# CREEM UN BUCLE WHILE PER A QUE PREGUNTI UN ALTRE COP SI L'USUARI NO ESCRIU 'SORTIR'
while resposta_paraula != "sortir":
    # SI LA PARAULA QUE HA ESCRIT L'USUARI SÍ QUE HI ES AL DICCIONARI...
    if resposta_paraula in diccionari_bilingue.keys():
        #...MOSTREM LA PARAULA I LA SEVA TRADUCCIÓ A L'ANGLÈS
        print(f"La traducció de '{resposta_paraula}' és: {diccionari_bilingue[resposta_paraula]}")
    else:
        # EN CAS DE QUE NO HI SIGUI, HO DIEM I PREGUNTEM SI LA VOL AFEGIR EL PROPI USUARI
        resposta_traduir = input("Aquesta paraula no hi és al diccionari. "
                                 "La vols afegir tu? (si/no) ").lower()
        # SI DIU QUE SÍ, LI DEMANEM LA TRADUCCIÓ I LA GUARDEM AL DICCIONARI
        if resposta_traduir == "si":
            traduccio = input(f"Escriu la traducció de '{resposta_paraula}': ")
            diccionari_bilingue.update({resposta_paraula: traduccio})

    resposta_paraula = input("Quina paraula vols traduir? Escriu 'sortir' quan hagis acabat: ").lower()