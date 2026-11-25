# Connectar el backend (FastAPI) amb el frontend (HTML/JS)

# 1. Com es parlen les dues parts

# El frontend i el backend són dos programes separats que es comuniquen per HTTP:
# Navegador (HTML + JS)  --- petició (fetch) --->  FastAPI
#                        <-- resposta en JSON ---

# El backend no dibuixa res, només retorna dades en JSON.
# El frontend demana aquestes dades amb JavaScript i les pinta a la pàgina.

# Els teus endpoints ja fan la seva part: GET /vehicles retorna una llista de
# diccionaris, i FastAPI la converteix sol a JSON.

# 2. CORS: el permís del navegador

# Si obres el teu HTML (per exemple des de Live Server, http://127.0.0.1:5500) i
# demana dades a la teva API (http://127.0.0.1:8000), el navegador ho bloqueja
# per seguretat, perquè són orígens diferents. Veuràs un error vermell que
# parla de CORS a la consola (F12).

# La solució és que el backend digui explícitament quins orígens deixa entrar.
# A FastAPI, afegeix això just després de app = FastAPI():

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # per practicar val tot; en producció es posa l'adreça real
    allow_methods=["*"],   # GET, POST, PUT, DELETE...
    allow_headers=["*"],
)
# Amb això el navegador ja deixa passar les peticions.

# 3. fetch: demanar dades des de JavaScript

# fetch fa la petició i retorna una promesa. De moment pensa-hi així: “demana,
# espera la resposta i després fes alguna cosa”. Amb async/await es llegeix de
# dalt a baix, com un codi normal:

# javascript
async function carregarVehicles() {
    # 1. Fem la petició al nostre backend
    const resposta = await fetch("http://127.0.0.1:8000/vehicles");

    # 2. Convertim la resposta de JSON a objectes de JavaScript
    const vehicles = await resposta.json();

    # 3. Ara 'vehicles' és una llista: la recorrem
    for (const v of vehicles) {
        console.log(v.MATRICULA, v.MARCA, v.MODEL);
    }
}

carregarVehicles();

# Fixa’t que v.MATRICULA s’escriu igual que el nom de la columna de la BD,
# perquè el dictionary=True del cursor fa que cada fila sigui
# {"MATRICULA": ..., "MARCA": ...}.

# Exemple mínim complet (HTML)

<!DOCTYPE html>
<html>
<body>
    <h1>Vehicles</h1>
    <ul id="llista"></ul>

    <script>
        async function carregarVehicles() {
            const resposta = await fetch("http://127.0.0.1:8000/vehicles");
            const vehicles = await resposta.json();

            const llista = document.getElementById("llista");
            for (const v of vehicles) {
                # Creem un <li> per cada vehicle i l'afegim a la llista
                const li = document.createElement("li");
                li.textContent = `${v.MATRICULA} - ${v.MARCA} ${v.MODEL} (${v.ESTAT})`;
                llista.appendChild(li);
            }
        }

        carregarVehicles();
    </script>
</body>
</html>

# Com provar-ho:

# Arrenca la API: uvicorn main:app --reload (canvia main pel nom del teu fitxer).
# Comprova que http://127.0.0.1:8000/vehicles et mostra el JSON al navegador.
# Obre el HTML i mira si apareix la llista. Si no, obre la consola (F12) i
# mira l’error.

# PREGUNTES IMPORTANTS

# 1. el arxiu .py amb el crud ha d'estar en el mateix directori que el .html?

# No, no cal. Són dos programes separats i es comuniquen per HTTP, així que
# cada fitxer pot estar on vulguis. El .py no sap on és el .html ni al
# revés: el HTML només necessita l’adreça de la API (http://127.0.0.1:8000).
# Una estructura ordenada per al projecte podria ser:
# gestor_flota/
# ├── backend/
# │   └── main.py
# └── frontend/
#     └── index.html

# Dues coses a tenir en compte:
# El .py s’arrenca des de la seva carpeta: cd backend i després
# uvicorn main:app --reload (on main és el nom del fitxer sense .py).
# El .html el pots obrir amb doble clic o amb Live Server, des d’on sigui.
# Si el CORS està ben posat, funcionarà igual.

# COM FER UN FETCH PER UN POST EN COMTES D'UN GET (afegir dades, no mostrar-les)

# 1. Què canvia respecte al GET
#
# Al GET només dius l'adreça. Al POST has d'afegir un segon paràmetre al
# fetch, un objecte amb les opcions:

fetch(url, {
    method: "POST",      # 1. quin tipus de petició és
    headers: {...},      # 2. com va empaquetada la informació
    body: ...            # 3. la informació que envies
})

# 2. Les 3 peces

# Peça	                   Què fa	                         Valor
# method	Diu que vols enviar dades (per defecte és GET)	 "POST"
# headers	Avisa el backend que el que envies és JSON	    {"Content-Type": "application/json"}
# body	    Les dades. Ha de ser text, no un objecte	     JSON.stringify(objecte)

# JSON.stringify converteix un objecte de JavaScript en text JSON. És el
# que fa FastAPI al revés quan et retorna les dades: ell converteix de
# Python a JSON, i tu converteixes de JS a JSON.

# 3. Un exemple petit, amb dades fixes

# Així veus la mecànica sense formulari:

async function afegirVehicleDeProva() {

    # L'objecte ha de tenir els MATEIXOS noms que el teu VehicleModel de Python
    # (en minúscules!): matricula, marca, model, estat, quilometratge
    const nouVehicle = {
        matricula: "1234QWE",
        marca: "Kia",
        model: "Ceed",
        estat: "DISPONIBLE",     # ha de ser un valor del teu Enum
        quilometratge: 1000      # un número, sense cometes
    }

    const resposta = await fetch("http://127.0.0.1:8000/vehicles", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(nouVehicle)
    })

    # Igual que al GET: primer mirem .ok, i després el .json()
    const dades = await resposta.json()

    if (!resposta.ok) {
        console.log("Error:", dades.detail)    # per ex. el 409 de matrícula duplicada
    } else {
        console.log(dades.missatge)           # "Vehicle afegit amb ID: ..."
    }
}

# Fixa't que la resposta es llegeix igual que al GET: .ok i .json(). El
# que has après al 7 també serveix aquí.

# Errors típics

# 422 en lloc de funcionar: els noms de l'objecte no coincideixen amb el
# model (MATRICULA en lloc de matricula), falta un camp, o quilometratge
# és un text.
# Oblidar JSON.stringify: et sortirà [object Object] o un 422.
# Oblidar el Content-Type: el backend no sap que és JSON.
# Provar-ho dues vegades: la segona et donarà el 409, perquè la matrícula
# ja existeix. Aprofita'l per veure que el missatge arriba a la consola.

# COM FER UN FETCH PER A UN PUT I UN DELETE

# PUT i DELETE des de JavaScript
# Poques idees noves: si saps fer el POST, ja saps el 90%. Només canvien
# tres coses.

# 1. Què canvia respecte al POST

# 	                   POST	       PUT	     DELETE
# Per a què	           Crear	  Editar	Esborrar
# method	           "POST"	  "PUT"	    "DELETE"
# Matrícula a la URL	 No	       Sí	       Sí
# headers i body	     Sí	       Sí	       No

# Això ve del teu backend:

@app.put("/vehicles/{matricula}")
# la matrícula va a la URL + dades al body
@app.delete("/vehicles/{matricula}")
# només la matrícula a la URL, sense body

# La regla és: al fetch es repeteix el que has escrit al @app. Si la
# ruta porta {matricula}, la URL la porta. Si la funció rep un model
# Pydantic (dades: VehicleUpdateModel), hi ha body.

# 2. PUT: editar

# Al teu backend només s'editen estat i quilometratge (el model
# VehicleUpdateModel). Per tant, el body només porta aquests dos camps:

async function editarVehicleDeProva() {

    const matricula = "1234ABC"                 // va a la URL

    const dadesNoves = {                        // va al body
        estat: "DISPONIBLE",                    // un valor del teu Enum
        quilometratge: 16000                    // un número
    }

    const resposta = await fetch(`http://127.0.0.1:8000/vehicles/${matricula}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(dadesNoves)
    })

    const dades = await resposta.json()

    if (!resposta.ok) {
        console.log("Error:", dades.detail)     // per ex. el 404 "Vehicle no trobat."
    } else {
        console.log(dades.missatge)
    }
}

# Fixa't que és idèntic al POST excepte el method i la matrícula a la URL.

# 3. DELETE: esborrar

# Aquí no s'envia res al body, només la matrícula a la URL. Per tant,
# no hi ha headers ni body:

async function eliminarVehicleDeProva() {

    const matricula = "1234ABC"

    const resposta = await fetch(`http://127.0.0.1:8000/vehicles/${matricula}`, {
        method: "DELETE"
    })

    const dades = await resposta.json()

    if (!resposta.ok) {
        console.log("Error:", dades.detail)
    } else {
        console.log(dades.missatge)
    }
}

# La resposta es llegeix igual que sempre: primer .ok, després .json().

# 4. Un detall important del DELETE

# A la teva BD, les taules RESERVES i MANTENIMENTS tenen ON DELETE CASCADE.
# Vol dir que si esborres un vehicle, s'esborren també totes les seves
# reserves i manteniments. Per provar, fes servir un vehicle que acabis
# de crear tu, no un de la BD original.
# A la web real, abans d'esborrar convé preguntar:

if (!confirm("Segur que vols donar de baixa aquest vehicle?")) {
    return
}

# confirm mostra un quadre amb Acceptar/Cancel·lar. Si prem Cancel·lar,
# return surt de la funció i no s'esborra res.

# 5. Errors típics

# 422 al PUT: falta el body, o el estat no és un valor del Enum
# ("EN TALLER", no "taller").
# 405: el method o la ruta no coincideixen amb el @app.
# 404: la matrícula no existeix (el backend ja la neteja amb .upper(),
# així que les majúscules no importen).
# Posar body al DELETE: no cal i no el fa servir.

# Resum per a la teva xuleta

# El fetch copia el @app del backend: el mètode, la ruta i, si la funció
# rep un model, el body.