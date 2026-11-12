# Exercici 5: La teva primera API "Hola Món"

# Objectiu: Instal·lar FastAPI i aixecar el teu primer servidor amb Uvicorn.
# Què has de fer: Crea un fitxer main.py, importa FastAPI, crea una ruta
# @app.get("/") que retorni un diccionari amb un missatge de benvinguda,
# i arrenca-ho amb uvicorn main:app --reload. Prova-ho al navegador i a /docs.

# IMPORTEM FASTAPI
from fastapi import FastAPI

# CREEM L'APP
app = FastAPI()

# FEM UN GET A CAP LLOC
@app.get("/")
# CREEM UNA FUNCIÓ QUE NOMÉS RETORNA UN MISSATGE DE BENVINGUDA
def donar_benvinguda():
    return {"message": "Hola Món!"}