# =====================================================================
# TEORIA CLAU: HTML, CSS I JAVASCRIPT PER AL PROJECTE
# =====================================================================
# Tot el fitxer son comentaris (#), aixi que pots tenir-lo obert en una
# pestanya al costat del teu codi (a PyCharm: clic dret a la pestanya ->
# "Split Right") i consultar-lo mentre pica codi.
#
# No t'ho has de llegir tot de cop. Cada bloc va amb els seus exercicis:
#
#   Exercicis 1-2   -> apartat 1 (HTML)
#   Exercicis 3-4   -> apartat 2 (CSS)
#   Exercicis 5-7   -> apartat 3 (JavaScript i DOM)
#   Exercicis 12-15 -> apartat 4 (fetch i CORS)
# =====================================================================


# =====================================================================
# 0. COM ENCAIXA TOT (LA CASA)
# =====================================================================
#
#   HTML       = l'estructura (parets, portes, finestres)  -> QUE hi ha
#   CSS        = la pintura i la decoracio                 -> COM es veu
#   JavaScript = l'electricitat                            -> QUE PASSA
#
# I com es relaciona amb l'API que ja saps fer:
#
#   Navegador (HTML+CSS+JS) --fetch (HTTP+JSON)--> API FastAPI --> MariaDB
#
# Igual que amb el restaurant: la pagina web es el CLIENT i la teva API
# es el CAMBRER. La pagina MAI parla directament amb la BD: el JavaScript
# fa una peticio a l'API, rep JSON i el pinta a la pagina.
#
# Que necessites: un editor (PyCharm/VS Code), un navegador i la
# CONSOLA DEL NAVEGADOR (tecla F12) per mirar errors.


# =====================================================================
# 1. HTML: L'ESTRUCTURA
# =====================================================================

# ---------------------------------------------------------------------
# 1.1 L'esquelet de tota pagina
# ---------------------------------------------------------------------
#
#   <!DOCTYPE html>
#   <html lang='ca'>
#     <head>
#       <!-- Informacio que NO es veu a la pagina -->
#       <meta charset='UTF-8'>
#       <title>Gestor de flota</title>
#       <link rel='stylesheet' href='estils.css'>   <!-- connecta el CSS -->
#     </head>
#     <body>
#       <!-- Tot el que SI es veu va aqui dins -->
#       <h1>Gestor de flota</h1>
#
#       <script src='app.js'></script>   <!-- connecta el JS, al FINAL -->
#     </body>
#   </html>
#
# Per que el <script> va al final del body? Perque el navegador llegeix
# la pagina de dalt a baix. Si el JS s'executa abans que existeixin els
# elements, no els trobara.

# ---------------------------------------------------------------------
# 1.2 Etiquetes i atributs
# ---------------------------------------------------------------------
# Una etiqueta s'obre i es tanca, i pot contenir text o altres etiquetes.
# Els ATRIBUTS donen informacio extra a l'etiqueta d'obertura:
#
#   <p id='intro' class='destacat'>Aixo es un paragraf</p>
#   # ^etiqueta   ^atribut id  ^atribut class
#
# Etiquetes que et caldran:
#
#   <h1> ... <h6>        Titols (h1 el mes important)
#   <p>                  Paragraf
#   <div>                Caixa generica per agrupar coses
#   <span>               Caixa generica dins d'una linia de text
#   <ul> / <li>          Llista / element de la llista
#   <table>              Taula sencera
#   <tr>                 Fila
#   <th>                 Cel.la de capcalera
#   <td>                 Cel.la normal
#   <form>, <input>, <select>, <button>, <label>   Formularis

# ---------------------------------------------------------------------
# 1.3 Taules
# ---------------------------------------------------------------------
# La taula s'escriu com una MATRIOIXCA: la taula conte files, i les files
# contenen cel.les.
#
#   <table>
#     <thead>   <!-- capcalera -->
#       <tr><th>Nom</th><th>Telefon</th></tr>
#     </thead>
#     <tbody>   <!-- cos: aqui aniran les dades -->
#       <tr><td>Carles Puig</td><td>600112233</td></tr>
#     </tbody>
#   </table>
#
# El <tbody> li posarem un id, perque mes endavant JavaScript hi anira
# afegint files.

# ---------------------------------------------------------------------
# 1.4 Formularis
# ---------------------------------------------------------------------
#
#   <form>
#     <label for='nom'>Nom:</label>
#     <input type='text' id='nom'>
#
#     <label for='inici'>Data d'inici:</label>
#     <input type='datetime-local' id='inici'>
#
#     <label for='estat'>Estat:</label>
#     <select id='estat'>
#       <option value='ACTIVA'>Activa</option>
#       <option value='PENDENT'>Pendent</option>
#     </select>
#
#     <button type='button' id='btn-enviar'>Enviar</button>
#   </form>
#
# A recordar:
#  - type canvia el tipus de camp: text, number, datetime-local, checkbox...
#  - <select> es fa amb <option>: el 'value' es el que llegira el JS, i el
#    text entre etiquetes es el que veu l'usuari.
#  - <label for='nom'> queda enllacat amb el camp que te id='nom'.
#  - Posa type='button' al boto: aixi no recarrega la pagina quan el
#    prems (un <button> dins d'un form per defecte l'envia i la recarrega).

# ---------------------------------------------------------------------
# 1.5 id vs class
# ---------------------------------------------------------------------
#  - id    : nom UNIC. Nomes un element a la pagina el pot tenir.
#            Serveix per TROBAR-LO des de JavaScript.
#  - class : nom REPETIBLE. Molts elements poden compartir-lo.
#            Serveix per donar-los el mateix ESTIL des de CSS.


# =====================================================================
# 2. CSS: L'ASPECTE
# =====================================================================

# ---------------------------------------------------------------------
# 2.1 La regla basica
# ---------------------------------------------------------------------
#
#   selector {
#     propietat: valor;
#     altra-propietat: valor;
#   }

# ---------------------------------------------------------------------
# 2.2 Els tres selectors que necessites
# ---------------------------------------------------------------------
#
#   /* 1. Per etiqueta: afecta TOTS els <td> */
#   td { padding: 8px; }
#
#   /* 2. Per classe (amb punt): afecta els que tenen class='disponible' */
#   .disponible { background-color: lightgreen; }
#
#   /* 3. Per id (amb coixinet): afecta l'unic element amb aquest id */
#   #intro { font-size: 18px; }

# ---------------------------------------------------------------------
# 2.3 Propietats que faras servir
# ---------------------------------------------------------------------
#
#   color              Color del text
#   background-color   Color de fons
#   font-family, font-size, font-weight   Tipus, mida i negreta del text
#   border             Vora: 1px solid black  (gruix, tipus, color)
#   padding            Espai INTERIOR (entre la vora i el contingut)
#   margin             Espai EXTERIOR (entre la caixa i les altres)
#   width, height      Mida de la caixa
#   text-align         Alineacio del text: left, center, right
#
# Per a taules: border-collapse: collapse;  al 'table' fa que les vores
# de les cel.les es fusionin en una de sola (si no, es veuen dobles).

# ---------------------------------------------------------------------
# 2.4 Els colors
# ---------------------------------------------------------------------
# Es poden escriure de tres maneres equivalents:
#   pel nom: red    en hexadecimal: #ff0000    amb rgb(255, 0, 0)

# ---------------------------------------------------------------------
# 2.5 Per que les classes son la clau del projecte
# ---------------------------------------------------------------------
# Si vols que cada estat tingui un color, no pintis les files una per una.
# Defineix una classe per estat al CSS, i despres nomes cal posar-li la
# classe correcta a l'element (a l'HTML o des de JS):
#
#   /* CSS */
#   .estat-ok { color: green; }
#
#   <!-- HTML -->
#   <td class='estat-ok'>text</td>
#
# Aixo es el que despres fara JavaScript: decidir quina classe posar
# segons el valor que rep de l'API.

# ---------------------------------------------------------------------
# 2.6 La caixa (box model)
# ---------------------------------------------------------------------
# Tot element es una caixa amb capes, de dins cap a fora:
#
#   contingut -> padding -> border -> margin
#
# Si una cosa no queda separada com vols, gairebe sempre es questio de
# padding (dins) o margin (fora).

# ---------------------------------------------------------------------
# 2.7 Flexbox (nomes si vols alinear coses; no cal que ho aprenguis ara)
# ---------------------------------------------------------------------
#
#   .fila { display: flex; gap: 10px; }
#
# Els elements que hi ha dins de .fila es posen un al costat de l'altre
# amb 10px de separacio.


# =====================================================================
# 3. JAVASCRIPT: LA LOGICA
# =====================================================================
# Si saps Python, saps l'important: nomes canvia la sintaxi.

# ---------------------------------------------------------------------
# 3.1 Python vs JavaScript
# ---------------------------------------------------------------------
#
#   PYTHON                      JAVASCRIPT
#   x = 5                       let x = 5;  /  const x = 5;  (const no canvia)
#   True / False / None         true / false / null
#   print(x)                    console.log(x)
#   if x > 5:                   if (x > 5) { ... }
#   elif / else                 else if / else
#   and / or / not              &&  /  ||  /  !
#   ==                          ===   (comparacio estricta, usa sempre aquesta)
#   llista [1, 2]               array [1, 2]
#   diccionari {'a': 1}         objecte {a: 1}
#   f'Hola {nom}'               `Hola ${nom}`  (amb accents oberts, no cometes)
#   def suma(a, b):             function suma(a, b) { ... }
#   for v in llista:            for (const v of llista) { ... }
#   len(llista)                 llista.length
#   llista.append(x)            llista.push(x)
#
# Els blocs es marquen amb { } en lloc d'indentacio, i les linies acaben
# amb ; (opcional, pero recomanat).

# ---------------------------------------------------------------------
# 3.2 Arrays i objectes (es el JSON!)
# ---------------------------------------------------------------------
# Un objecte de JS es com un diccionari de Python, i el que et torna la
# teva API (JSON) es converteix en arrays i objectes de JS:
#
#   const conductor = { nom: 'Carles', telefon: '600112233' };
#   console.log(conductor.nom);       // 'Carles'
#
#   const conductors = [
#     { nom: 'Carles', actiu: true },
#     { nom: 'Marta',  actiu: false }
#   ];
#   console.log(conductors[1].nom);   // 'Marta'

# ---------------------------------------------------------------------
# 3.3 Funcions i bucles
# ---------------------------------------------------------------------
#
#   function saluda(nom) {
#     return `Hola, ${nom}!`;
#   }
#
#   for (const c of conductors) {
#     console.log(c.nom);
#   }
#
#   // Funcio fletxa: una manera curta d'escriure una funcio
#   const doble = (n) => n * 2;

# ---------------------------------------------------------------------
# 3.4 Metodes utils d'arrays
# ---------------------------------------------------------------------
#
#   // filter: et quedes nomes amb els que compleixen una condicio
#   const actius = conductors.filter(c => c.actiu === true);
#
#   // map: transforma cada element en un altre
#   const noms = conductors.map(c => c.nom);   // ['Carles', 'Marta']
#
# Amb  c => c.actiu , la 'c' es cada element mentre recorre la llista
# (com la 'v' del  for v in llista  de Python).

# ---------------------------------------------------------------------
# 3.5 El DOM: com JavaScript toca l'HTML
# ---------------------------------------------------------------------
# El DOM es la pagina HTML convertida en objectes que JS pot llegir i
# modificar. El patro sempre es el mateix:
#
#   1) TROBAR l'element    2) LLEGIR-LO o CANVIAR-LO
#
#   // 1. Trobar
#   const titol = document.getElementById('titol');
#
#   // 2. Canviar
#   titol.textContent = 'Nou text';        // canvia el text
#   titol.classList.add('destacat');       // afegeix una classe CSS
#   titol.classList.remove('destacat');    // la treu
#
#   // Llegir el que ha escrit l'usuari en un camp d'un formulari
#   const valor = document.getElementById('nom').value;
#
# Per afegir contingut HTML dins d'un element (per exemple, files a una
# taula):
#
#   const cos = document.getElementById('cos-taula');
#   cos.innerHTML = '';                            // buida
#   cos.innerHTML += `<tr><td>${nom}</td></tr>`;   // afegeix una fila
#
# textContent es per a text net. innerHTML interpreta les etiquetes HTML.
# Amb innerHTML i dades que venen de fora, si una dada continguees codi
# HTML el navegador l'executaria: per al teu projecte, amb dades de la
# teva BD, es acceptable, pero convé saber-ho.

# ---------------------------------------------------------------------
# 3.6 Esdeveniments: reaccionar a l'usuari
# ---------------------------------------------------------------------
# Un esdeveniment es "alguna cosa que ha passat a la pagina" (un clic, un
# canvi en un desplegable...). Li dius a un element: QUAN passi X,
# EXECUTA aquesta funcio.
#
#   const boto = document.getElementById('btn-amagar');
#
#   boto.addEventListener('click', () => {
#     const caixa = document.getElementById('caixa');
#     caixa.classList.toggle('amagat');   // toggle: la posa si no hi es,
#   });                                   // la treu si hi es
#
# Per als desplegables (<select>) l'esdeveniment util es 'change': salta
# quan l'usuari tria una altra opcio.

# ---------------------------------------------------------------------
# 3.7 La consola (F12)
# ---------------------------------------------------------------------
# Es la teva millor amiga, com el terminal d'uvicorn per a l'API. Si la
# pagina no fa res, obre F12 -> pestanya Console i mira els errors en
# vermell. console.log(variable) es el 'print' per veure que val una cosa.


# =====================================================================
# 4. CONNECTAR LA WEB AMB LA TEVA API
# =====================================================================

# ---------------------------------------------------------------------
# 4.1 fetch: el que feia 'requests' a Python
# ---------------------------------------------------------------------
# fetch envia una peticio HTTP des del navegador. Te una particularitat:
# es ASINCRON. Vol dir que la resposta triga una mica en arribar (xarxa,
# BD...) i JS no es queda aturat esperant. Per gestionar-ho:
#
#   - 'async' davant de la funcio diu "aquesta funcio fara coses que triguen"
#   - 'await' davant d'una peticio diu "espera aqui fins que arribi la resposta"

# ---------------------------------------------------------------------
# 4.2 GET (llegir dades)
# ---------------------------------------------------------------------
#
#   async function carregarConductors() {
#     const resposta = await fetch('http://127.0.0.1:8000/conductors');
#
#     if (!resposta.ok) {                    // ok es true si el codi es 2xx
#       console.log('Error', resposta.status);
#       return;
#     }
#
#     const dades = await resposta.json();   // converteix el JSON en array/objecte
#     console.log(dades);
#   }
#
#   carregarConductors();   // cal cridar la funcio perque s'executi
#
# Fixa't que resposta.json() tambe porta 'await'.

# ---------------------------------------------------------------------
# 4.3 POST (enviar dades)
# ---------------------------------------------------------------------
# Igual que a /docs o a requests, cal enviar el JSON al cos de la peticio.
# A fetch s'ha d'indicar el metode, la capcalera i el cos, i el cos s'ha
# de convertir a text amb JSON.stringify:
#
#   async function crearConductor() {
#     const nou = { nom: 'Carles Puig', carnet: '12345678Z', telefon: '600112233' };
#
#     const resposta = await fetch('http://127.0.0.1:8000/conductors', {
#       method: 'POST',
#       headers: { 'Content-Type': 'application/json' },
#       body: JSON.stringify(nou)
#     });
#
#     const dades = await resposta.json();
#     console.log(resposta.status, dades);
#   }
#
# Els noms dels camps del JSON han de coincidir exactament amb els del
# teu model Pydantic de l'API (nom, carnet, telefon), si no, rebras un 422.

# ---------------------------------------------------------------------
# 4.4 L'error de CORS
# ---------------------------------------------------------------------
# Quan la pagina web (oberta des d'un fitxer o des d'un altre port)
# intenta parlar amb la teva API (127.0.0.1:8000), el navegador la bloqueja
# per seguretat i a la consola (F12) veuras un error que parla de CORS.
#
#  - NO es un error del teu codi JS: es el navegador protegint l'usuari.
#  - La solucio va a l'API, no a la web: li has de dir a FastAPI que
#    permet peticions des d'altres origens (hi ha un "middleware" per a
#    aixo: CORSMiddleware).
#  - Ho resoldras a l'exercici 13. Mentrestant, si veus aquest error, ja
#    saps que es.

# ---------------------------------------------------------------------
# 4.5 El flux complet
# ---------------------------------------------------------------------
#   1. L'usuari prem un boto                          (ESDEVENIMENT)
#   2. JS fa una peticio a l'API                      (FETCH)
#   3. L'API consulta la BD i retorna JSON
#   4. JS rep l'array, el recorre amb un bucle i
#      crea l'HTML                                    (DOM)
#   5. El CSS decideix quin aspecte te                (CLASSES)


# =====================================================================
# 5. ERRORS TIPICS (I ON MIRAR)
# =====================================================================
#
#   QUE PASSA                          CAUSA PROBABLE
#   --------------------------------   ---------------------------------------
#   El JS no fa res                    Error a la consola (F12), o el <script>
#                                      esta abans que els elements
#   Cannot read properties of null     getElementById no ha trobat l'element:
#                                      comprova que l'id coincideix exactament
#   El boto recarrega la pagina        Falta type='button'
#   'undefined' en lloc del valor      El nom del camp no coincideix amb el del
#                                      JSON (compte amb majuscules: amb
#                                      SELECT * i dictionary=True els camps
#                                      surten tal com estan a la BD, p. ex.
#                                      MATRICULA en majuscules)
#   Error de CORS                      Falta configurar CORS a l'API
#   422 en un POST                     El JSON enviat no coincideix amb el
#                                      model Pydantic
#   500 en un POST                     Mira el terminal d'uvicorn: l'error
#                                      real es alla
#
# REGLA D'OR: mira sempre dos llocs.
#   - El navegador (F12) per als errors de la web.
#   - El terminal d'uvicorn per als errors de l'API.