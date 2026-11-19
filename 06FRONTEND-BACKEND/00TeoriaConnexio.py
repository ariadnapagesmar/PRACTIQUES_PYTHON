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
