# =====================================================================
# HTML, CSS I JAVASCRIPT DES DE ZERO
# =====================================================================
# Sense Python, sense APIs i sense bases de dades. Només pàgines web.
#
# COM UTILITZAR AQUEST FITXER
#  - Tot són comentaris (#): el pots tenir obert en una pestanya al costat
#    del teu codi (clic dret a la pestanya -> Split Right).
#  - Cada lliçó és PETITA i porta una línia "PROVA-HO". No passis a la
#    següent fins que la prova t'hagi sortit.
#  - Si una lliçó no t'entra, torna enrere o demana'm un exemple més.
#
# ORDRE: primer HTML (la part 1), després CSS (la 2), després JS (la 3).
# Cada part es pot fer en dies diferents.
#
#   PART 0  Preparar el terreny
#   PART 1  HTML  (l'estructura)   lliçons 1.1 - 1.12
#   PART 2  CSS   (l'aspecte)      lliçons 2.1 - 2.8
#   PART 3  JS    (el comportament) lliçons 3.1 - 3.14
# =====================================================================


# =====================================================================
# PART 0. PREPARAR EL TERRENY
# =====================================================================
#
# Què són les tres coses? Pensa en una casa:
#
#   HTML       = l'estructura (parets, portes, finestres)   -> QUÈ hi ha
#   CSS        = la pintura i la decoració                  -> COM es veu
#   JavaScript = l'electricitat                             -> QUÈ PASSA
#
# Crearàs una carpeta per a les proves, per exemple "proves_web", amb
# aquests tres fitxers (de moment en crearem només un):
#
#   proves_web/
#       pagina.html     <- HTML
#       estils.css      <- CSS (a la part 2)
#       app.js          <- JavaScript (a la part 3)
#
# Com veure el resultat: fes doble clic al fitxer .html i s'obrirà al
# navegador. Cada vegada que facis un canvi i el guardis, torna al
# navegador i prem F5 (refrescar).
#
# La consola (tecla F12 al navegador) serveix per veure errors. De moment
# no cal que hi vagis.


# =====================================================================
# PART 1. HTML: L'ESTRUCTURA
# =====================================================================

# ---------------------------------------------------------------------
# 1.1 Què és HTML
# ---------------------------------------------------------------------
# És un text normal escrit amb ETIQUETES. Les etiquetes diuen al
# navegador què és cada cosa: això és un títol, això és un paràgraf...
#
# Una etiqueta s'escriu entre < >, i normalment s'OBRE i es TANCA:
#
#   <p>Hola, soc un paràgraf</p>
#   ^^^                      ^^^^
#   obre                     tanca (porta una barra /)
#
# Tot el que hi ha entre les dues és el contingut de l'etiqueta.

# ---------------------------------------------------------------------
# 1.2 El teu primer fitxer
# ---------------------------------------------------------------------
# Crea "pagina.html" i escriu-hi això (sempre comença igual):
#
#   <!DOCTYPE html>
#   <html lang='ca'>
#     <head>
#       <meta charset='UTF-8'>
#       <title>La meva pàgina</title>
#     </head>
#     <body>
#       <h1>Hola món</h1>
#     </body>
#   </html>
#
# Línia per línia:
#   <!DOCTYPE html>        Diu al navegador "això és HTML modern".
#   <html lang='ca'>       Tot el contingut va dins. 'ca' = en català.
#   <head>                 Informació que NO es veu a la pàgina.
#   <meta charset='UTF-8'> Perquè es vegin bé els accents i la ç.
#   <title>                El text de la pestanya del navegador.
#   <body>                 Tot el que SÍ es veu va aquí dins.
#
# Ara mateix només has de fixar-te en una cosa: tot el que vulguis veure
# a la pàgina l'escriuràs DINS del <body>.
#
# PROVA-HO: obre el fitxer amb doble clic. Has de veure "Hola món" en gran
# i la pestanya amb el títol "La meva pàgina".

# ---------------------------------------------------------------------
# 1.3 Títols i paràgrafs
# ---------------------------------------------------------------------
#   <h1>Títol principal</h1>
#   <h2>Subtítol</h2>
#   <h3>Subtítol més petit</h3>
#   <p>Això és un paràgraf de text.</p>
#   <p>Això és un altre paràgraf.</p>
#
# h1 és el més gran i important, i va baixant fins a h6. Cada <p> és un
# paràgraf separat.
#
# PROVA-HO: dins del <body>, escriu un h1, un h2 i dos paràgrafs sobre
# el que vulguis (la teva mascota, el teu menjar preferit...).

# ---------------------------------------------------------------------
# 1.4 Negreta, cursiva i salt de línia
# ---------------------------------------------------------------------
#   <p>Això és <strong>important</strong> i això és <em>suau</em>.</p>
#   <p>Primera línia<br>Segona línia</p>
#
#   <strong>   negreta
#   <em>       cursiva
#   <br>       salt de línia (no es tanca)
#
# Fixa't que <strong> va DINS del <p>: les etiquetes es poden posar unes
# dins de les altres (ho veurem a la 1.7).
#
# PROVA-HO: posa una paraula en negreta i una altra en cursiva a un dels
# teus paràgrafs.

# ---------------------------------------------------------------------
# 1.5 Llistes
# ---------------------------------------------------------------------
#   <ul>
#     <li>Pa</li>
#     <li>Llet</li>
#     <li>Ous</li>
#   </ul>
#
#   <ul>  llista amb punts        <ol>  llista numerada (1, 2, 3...)
#   <li>  cada element de la llista
#
# PROVA-HO: fes una llista amb 3 coses. Després canvia <ul> per <ol>
# (a l'inici i al final) i mira què passa.

# ---------------------------------------------------------------------
# 1.6 Enllaços i imatges
# ---------------------------------------------------------------------
#   <a href='https://www.wikipedia.org'>Ves a la Viquipèdia</a>
#   <img src='gat.jpg' alt='Una foto d'un gat'>
#
# Aquí apareixen els ATRIBUTS: informació extra dins de l'etiqueta
# d'obertura, amb la forma nom='valor'.
#
#   <a href='...'>        a on porta l'enllaç (href = destí)
#   <img src='...'>       quin fitxer d'imatge es mostra
#   alt='...'             text que descriu la imatge (no es tanca <img>)
#
# La imatge ha d'estar a la mateixa carpeta que el fitxer HTML.
#
# PROVA-HO: afegeix un enllaç a una web que t'agradi.

# ---------------------------------------------------------------------
# 1.7 Etiquetes dins d'etiquetes
# ---------------------------------------------------------------------
# Aquest és EL concepte més important d'HTML. Les etiquetes es posen unes
# dins de les altres, com capses dins de capses:
#
#   <ul>                      <- capsa gran
#     <li>Pa <strong>integral</strong></li>   <- capsa mitjana, amb una de petita
#     <li>Llet</li>
#   </ul>
#
# Regla: la que s'obre l'última, es tanca la primera.
#
#   CORRECTE:    <p><strong>text</strong></p>
#   INCORRECTE:  <p><strong>text</p></strong>
#
# I per això s'indenta (es deixen espais): perquè es vegi què va dins de què.
#
# PROVA-HO: a la llista de la 1.5, posa una paraula en negreta dins d'un
# <li>.

# ---------------------------------------------------------------------
# 1.8 div i span: les caixes genèriques
# ---------------------------------------------------------------------
#   <div>
#     <h2>La meva mascota</h2>
#     <p>Es diu <span>Lluna</span> i és una gata.</p>
#   </div>
#
#   <div>   caixa per AGRUPAR coses (ocupa tota la línia)
#   <span>  caixa petita dins d'una línia de text
#
# No es veuen per si soles, però serveixen per agrupar i, més endavant,
# per donar-los estil amb CSS.
#
# PROVA-HO: agrupa un títol i dos paràgrafs dins d'un <div>.

# ---------------------------------------------------------------------
# 1.9 id i class
# ---------------------------------------------------------------------
# Són dos atributs que poden portar TOTES les etiquetes. Serveixen per
# "posar-los nom" i trobar-los després des de CSS i JavaScript.
#
#   <p id='intro'>Aquest paràgraf té un id.</p>
#   <p class='destacat'>Aquest té una classe.</p>
#   <p class='destacat'>I aquest també la mateixa classe.</p>
#
#   id     -> nom ÚNIC. Només UN element de la pàgina el pot tenir.
#   class  -> nom REPETIBLE. Molts elements poden compartir-lo.
#
# De moment només escriu-los; no fan res visible fins que arribem a CSS
# i JS.
#
# PROVA-HO: posa un id a un paràgraf i una classe a dos altres.

# ---------------------------------------------------------------------
# 1.10 Taules (pas a pas)
# ---------------------------------------------------------------------
# Una taula té FILES, i les files tenen CEL·LES. Ho farem en 3 passos.
#
# PAS 1: una fila amb una cel·la
#   <table>
#     <tr>
#       <td>Lluna</td>
#     </tr>
#   </table>
#
#   <table>  la taula sencera
#   <tr>     una FILA (de "table row")
#   <td>     una CEL·LA (de "table data")
#
# PAS 2: una fila amb 3 cel·les (les cel·les van una al costat de l'altra)
#   <tr>
#     <td>Lluna</td>
#     <td>Gata</td>
#     <td>3 anys</td>
#   </tr>
#
# PAS 3: afegeix una fila de capçalera amb <th> (és com <td> però en
#        negreta i centrada) i més files:
#   <table>
#     <tr>
#       <th>Nom</th>
#       <th>Espècie</th>
#       <th>Edat</th>
#     </tr>
#     <tr>
#       <td>Lluna</td>
#       <td>Gata</td>
#       <td>3 anys</td>
#     </tr>
#     <tr>
#       <td>Rex</td>
#       <td>Gos</td>
#       <td>5 anys</td>
#     </tr>
#   </table>
#
# Regla: cada <tr> és una fila, i dins de cada fila tantes cel·les com
# columnes vulguis. Totes les files han de tenir el mateix nombre de
# cel·les.
#
# PROVA-HO: fes una taula de 3 files i 3 columnes amb el que vulguis
# (pel·lícules, amics...). De moment no tindrà vores: és normal.

# ---------------------------------------------------------------------
# 1.11 Formularis: camps de text i números (pas a pas)
# ---------------------------------------------------------------------
# Un formulari és una pàgina on l'usuari POT ESCRIURE coses. Cada casella
# és un <input>.
#
# PAS 1: una casella de text
#   <input type='text'>
#
# Una casella sense res més no diu què s'hi ha d'escriure. Afegim un
# <label> (l'etiqueta de text que veu l'usuari) i un id:
#
#   <label for='nom'>Nom:</label>
#   <input type='text' id='nom'>
#
#   - <label> és el text que acompanya la casella.
#   - for='nom' l'enllaça amb la casella que té id='nom'. Han de coincidir.
#   - <input> no es tanca (no porta </input>).
#
# PAS 2: una casella de número
#   <label for='edat'>Edat:</label>
#   <input type='number' id='edat'>
#
#   type='number' només deixa escriure números i posa fletxetes.
#
# PAS 3: una casella de data
#   <label for='aniversari'>Aniversari:</label>
#   <input type='date' id='aniversari'>
#
#   type='date' mostra un calendari.
#
# Els tipus d'input més comuns: text, number, date, password, checkbox.
#
# PROVA-HO: fes un formulari amb tres caselles: nom (text), edat (number)
# i aniversari (date). Escriu-hi coses per veure que funcionen. Un truc:
# posa cada parella label+input dins d'un <div> perquè quedin en línies
# separades.

# ---------------------------------------------------------------------
# 1.12 Formularis: botó i desplegable
# ---------------------------------------------------------------------
# EL BOTÓ
#   <button type='button'>Enviar</button>
#
# type='button' vol dir "és un botó normal". De moment, no fa res en
# prémer-lo (això ho farà JavaScript a la part 3).
#
# EL DESPLEGABLE (<select>)
# Aquest és diferent: no és un <input>. És una capsa (<select>) amb
# opcions a dins (<option>).
#
#   <label for='color'>Color preferit:</label>
#   <select id='color'>
#     <option value='VERMELL'>Vermell</option>
#     <option value='BLAU'>Blau</option>
#     <option value='VERD'>Verd</option>
#   </select>
#
#   <select>  el desplegable sencer
#   <option>  cada opció
#   value     el valor "intern" (el que després llegirà JavaScript)
#   el text entre etiquetes (Vermell) és el que VEU l'usuari
#
# Quan l'usuari tria "Vermell", per a JavaScript el valor serà VERMELL.
# Normalment són semblants, però no cal que siguin iguals.
#
# PROVA-HO: afegeix al formulari anterior un desplegable amb 3 opcions i
# un botó. Prem el botó: no passarà res, i està bé.
#
# FINAL DE LA PART 1: ja saps escriure pàgines amb títols, text, llistes,
# taules i formularis. Tot el que ve ara és donar-li aspecte (CSS) i vida
# (JS).


# =====================================================================
# PART 2. CSS: L'ASPECTE
# =====================================================================

# ---------------------------------------------------------------------
# 2.1 Què és CSS i com es connecta
# ---------------------------------------------------------------------
# CSS diu COM es veu cada cosa: colors, mides, espais. S'escriu en un
# fitxer a part, "estils.css", i es connecta des de l'HTML amb una línia
# dins del <head>:
#
#   <head>
#     <meta charset='UTF-8'>
#     <title>La meva pàgina</title>
#     <link rel='stylesheet' href='estils.css'>
#   </head>
#
# Crea "estils.css" a la mateixa carpeta. Ha d'estar buit de moment.
#
# PROVA-HO: afegeix la línia <link ...> al teu HTML i crea el fitxer CSS.

# ---------------------------------------------------------------------
# 2.2 La primera regla
# ---------------------------------------------------------------------
# Una regla CSS té aquesta forma:
#
#   selector {
#     propietat: valor;
#   }
#
#   - selector:  A QUÈ vols donar estil
#   - propietat: QUÈ vols canviar
#   - valor:     QUIN valor li poses
#   - cada línia acaba amb ;
#
# Exemple: "tots els <h1> en color vermell":
#
#   h1 {
#     color: red;
#   }
#
# PROVA-HO: escriu aquesta regla a estils.css, desa i refresca el
# navegador (F5). El títol ha de sortir vermell.

# ---------------------------------------------------------------------
# 2.3 Els tres selectors
# ---------------------------------------------------------------------
# El selector diu a QUINS elements s'aplica. Només en necessites tres:
#
#   /* 1. Per etiqueta: afecta TOTES les etiquetes d'aquell tipus */
#   p {
#     color: gray;
#   }
#
#   /* 2. Per classe (amb punt): afecta els que tenen class='destacat' */
#   .destacat {
#     color: orange;
#   }
#
#   /* 3. Per id (amb coixinet #): afecta l'únic amb id='intro' */
#   #intro {
#     color: blue;
#   }
#
# Aquí és on serveixen les class i els id de la lliçó 1.9. Els comentaris
# en CSS s'escriuen amb /* ... */.
#
# PROVA-HO: fes que tots els paràgrafs siguin grisos, els de classe
# 'destacat' taronges, i el de l'id 'intro' blau.

# ---------------------------------------------------------------------
# 2.4 Colors i text
# ---------------------------------------------------------------------
#   color:            color del text
#   background-color: color de fons
#   font-size:        mida del text (ex: 20px)
#   font-weight:      bold (negreta) o normal
#   font-family:      tipus de lletra (ex: Arial, sans-serif)
#   text-align:       left, center, right
#
# Els colors es poden escriure de tres maneres:
#   pel nom: red, blue, lightgreen
#   en hexadecimal: #ff0000
#   amb rgb(255, 0, 0)
#
# Exemple:
#
#   h1 {
#     color: white;
#     background-color: darkblue;
#     text-align: center;
#     font-family: Arial, sans-serif;
#   }
#
# PROVA-HO: dona al h1 fons fosc, lletra blanca i centrat.

# ---------------------------------------------------------------------
# 2.5 La caixa: padding, border i margin
# ---------------------------------------------------------------------
# Cada element és una CAIXA amb capes. De dins cap a fora:
#
#   contingut -> padding -> border -> margin
#
#   padding: espai ENTRE el contingut i la vora (aire dins)
#   border:  la vora
#   margin:  espai ENTRE la caixa i les altres (aire fora)
#
# Exemple:
#
#   .targeta {
#     border: 2px solid black;     /* gruix, tipus, color */
#     padding: 15px;
#     margin: 10px;
#   }
#
# I a l'HTML:  <div class='targeta'> ... </div>
#
# Truc: si una cosa "no respira" per dins, puja el padding. Si està massa
# enganxada a les altres, puja el margin.
#
# PROVA-HO: fes una classe .targeta i aplica-la a un <div> amb text.

# ---------------------------------------------------------------------
# 2.6 Mida
# ---------------------------------------------------------------------
#   width:   amplada (ex: 300px, o 50% de l'espai disponible)
#   height:  alçada
#
#   .targeta {
#     width: 300px;
#   }
#
# PROVA-HO: dona una amplada de 300px a la teva targeta.

# ---------------------------------------------------------------------
# 2.7 Donar estil a una taula
# ---------------------------------------------------------------------
# Per defecte les taules no tenen vores. Tu les poses amb CSS:
#
#   table {
#     border-collapse: collapse;   /* fusiona les vores en una sola */
#   }
#
#   th, td {                       /* la coma = "tant th com td" */
#     border: 1px solid black;
#     padding: 8px;
#   }
#
#   th {
#     background-color: lightgray;
#   }
#
# Sense border-collapse les vores es veuen dobles.
#
# PROVA-HO: dona vores, espai i fons de capçalera a la taula de la 1.10.

# ---------------------------------------------------------------------
# 2.8 Una classe per cada "estat"
# ---------------------------------------------------------------------
# Les classes serveixen per aplicar el mateix estil a molts elements.
# Per exemple, per marcar productes segons si n'hi ha o no:
#
#   .hi-ha     { color: green; }
#   .no-hi-ha  { color: red; }
#
# I a l'HTML:
#
#   <p class='hi-ha'>Pa</p>
#   <p class='no-hi-ha'>Llet</p>
#   <p class='hi-ha'>Ous</p>
#
# Si algun dia vols canviar el verd per un altre, només ho fas en un lloc.
# I després, JavaScript podrà posar i treure classes per canviar l'estil.
#
# PROVA-HO: fes dues classes de colors diferents i aplica-les a una
# llista.
#
# FINAL DE LA PART 2: ja saps connectar CSS, usar selectors, i canviar
# colors, text, espais i taules.


# =====================================================================
# PART 3. JAVASCRIPT: EL COMPORTAMENT
# =====================================================================
# Si ja saps Python, saps l'important: les idees són les mateixes. Només
# canvia com s'escriu.

# ---------------------------------------------------------------------
# 3.1 Què és JS i com es connecta
# ---------------------------------------------------------------------
# JavaScript fa que la pàgina REACCIONI (botons, canvis, càlculs). S'escriu
# en un fitxer a part, "app.js", i es connecta al FINAL del <body>:
#
#     ...
#     <script src='app.js'></script>
#   </body>
#
# Per què al final? Perquè el navegador llegeix l'HTML de dalt a baix. Si
# el JS s'executa abans que existeixin els elements, no els trobarà.
#
# Crea "app.js" a la mateixa carpeta. Dins escriu:
#
#   console.log('Hola des de JavaScript');
#
# console.log és l'equivalent del print de Python: escriu coses a la
# consola. Per veure-la: obre la pàgina, prem F12 i ves a la pestanya
# "Console" (o "Consola").
#
# PROVA-HO: connecta el script, obre la consola i mira que surt el missatge.
# Si no surt, comprova el nom del fitxer i que has desat els canvis.

# ---------------------------------------------------------------------
# 3.2 Variables
# ---------------------------------------------------------------------
#   let edat = 20;              // una variable que pot canviar
#   const nom = 'Ariadna';      // una variable que NO canviarà
#   edat = 21;                  // així la canvies (només amb let)
#
#   console.log(nom);
#   console.log(edat);
#
# Equivalències amb Python:
#   Python:  nom = 'Ariadna'        JS:  const nom = 'Ariadna';
#   Python:  True / False / None    JS:  true / false / null
#   Python:  # comentari            JS:  // comentari
#
# Cada línia acaba amb ; (en Python no).
#
# PROVA-HO: crea tres variables i escriu-les a la consola.

# ---------------------------------------------------------------------
# 3.3 Operacions i text amb variables
# ---------------------------------------------------------------------
#   const a = 10;
#   const b = 3;
#   console.log(a + b);     // 13
#   console.log(a * b);     // 30
#
# Per posar variables dins d'un text, s'utilitzen els ACCENTS OBERTS (`)
# i ${ }. Equival a l'f'...' de Python:
#
#   const nom = 'Ariadna';
#   console.log(`Hola, ${nom}!`);        // Hola, Ariadna!
#
# Compte: han de ser accents oberts `, no cometes simples '.
#
# PROVA-HO: escriu "Tinc 20 anys" a la consola utilitzant una variable
# per a l'edat.

# ---------------------------------------------------------------------
# 3.4 Condicions: if / else
# ---------------------------------------------------------------------
#   const edat = 17;
#
#   if (edat >= 18) {
#     console.log('Majoria d\'edat');
#   } else {
#     console.log('Menor');
#   }
#
# Diferències amb Python:
#   - la condició va entre parèntesis ( )
#   - el bloc va entre claus { }, no amb indentació
#   - "elif" és "else if"
#   - per comparar si són iguals, s'utilitza === (tres signes igual)
#   - "and/or/not" són  &&  /  ||  /  !
#
# PROVA-HO: canvia el valor de edat i mira que el missatge canvia.

# ---------------------------------------------------------------------
# 3.5 Funcions
# ---------------------------------------------------------------------
#   function saluda(nom) {
#     return `Hola, ${nom}!`;
#   }
#
#   console.log(saluda('Ariadna'));
#
# És com el def de Python, però amb "function" i claus.
#
# PROVA-HO: fes una funció suma(a, b) que retorni la suma, i prova-la.

# ---------------------------------------------------------------------
# 3.6 Arrays (llistes)
# ---------------------------------------------------------------------
#   const fruites = ['poma', 'pera', 'plàtan'];
#
#   console.log(fruites[0]);          // poma (el primer és el 0, com a Python)
#   console.log(fruites.length);      // 3   (com len() a Python)
#   fruites.push('taronja');          // afegeix al final (append a Python)
#
# PROVA-HO: fes un array amb 4 coses, escriu la segona i afegeix-ne una.

# ---------------------------------------------------------------------
# 3.7 Bucles
# ---------------------------------------------------------------------
#   for (const fruita of fruites) {
#     console.log(fruita);
#   }
#
# És l'equivalent de  for fruita in fruites:  de Python. Cada volta,
# "fruita" val un element de la llista.
#
# PROVA-HO: recorre el teu array i escriu cada element a la consola.

# ---------------------------------------------------------------------
# 3.8 Objectes
# ---------------------------------------------------------------------
# Un objecte és com un diccionari de Python: agrupa dades amb nom.
#
#   const mascota = { nom: 'Lluna', espècie: 'gata', edat: 3 };
#
#   console.log(mascota.nom);       // Lluna  (amb un punt, no amb ['nom'])
#   mascota.edat = 4;               // modifica
#
# I es poden fer arrays d'objectes:
#
#   const mascotes = [
#     { nom: 'Lluna', edat: 3 },
#     { nom: 'Rex',   edat: 5 }
#   ];
#
#   console.log(mascotes[1].nom);   // Rex
#
#   for (const m of mascotes) {
#     console.log(`${m.nom} té ${m.edat} anys`);
#   }
#
# PROVA-HO: fes un array de 3 objectes (pel·lícules amb títol i any) i
# recorre'l escrivint cada títol.
#
# AQUÍ FINALITZA LA PART DE "JS SOL". Ara ve la part que el connecta amb
# la pàgina.

# ---------------------------------------------------------------------
# 3.9 El DOM: tocar la pàgina des de JS (trobar i canviar)
# ---------------------------------------------------------------------
# El navegador converteix el teu HTML en una estructura que JS pot
# llegir i modificar: el DOM. El patró sempre és el mateix, en 2 passos:
#
#   1) TROBAR l'element (pel seu id)
#   2) CANVIAR-LO
#
# Exemple. Al HTML:
#
#   <h1 id='titol'>Títol original</h1>
#
# Al JS:
#
#   const titol = document.getElementById('titol');   // 1. trobar
#   titol.textContent = 'Títol nou';                  // 2. canviar el text
#
# Obre la pàgina: el títol ja diu "Títol nou". JS l'ha canviat.
#
# IMPORTANT: el id de l'HTML i el del getElementById han de coincidir
# exactament (majúscules incloses).
#
# PROVA-HO: posa un id a un dels teus paràgrafs i canvia'n el text des de
# JS. Si no funciona, obre F12 i llegeix l'error en vermell.

# ---------------------------------------------------------------------
# 3.10 Esdeveniments: reaccionar a un clic
# ---------------------------------------------------------------------
# Un esdeveniment és "alguna cosa que ha passat a la pàgina": un clic, un
# canvi... Li dius a un element: QUAN passi això, EXECUTA aquesta funció.
#
# Al HTML:
#
#   <p id='missatge'>Encara no has fet clic</p>
#   <button id='boto'>Prem-me</button>
#
# Al JS:
#
#   const boto = document.getElementById('boto');
#   const missatge = document.getElementById('missatge');
#
#   boto.addEventListener('click', () => {
#     missatge.textContent = 'Has fet clic!';
#   });
#
# Què diu això: "al botó, quan hi hagi un 'click', fes el que hi ha entre
# les claus". El () => { ... } és una funció curta sense nom.
#
# PROVA-HO: fes que, en prémer un botó, canviï el text d'un paràgraf.

# ---------------------------------------------------------------------
# 3.11 Llegir el que escriu l'usuari
# ---------------------------------------------------------------------
# Per saber què ha escrit algú en una casella, s'utilitza .value:
#
# HTML:
#   <input type='text' id='nom'>
#   <button id='saludar'>Saludar</button>
#   <p id='resultat'></p>
#
# JS:
#   const camp = document.getElementById('nom');
#   const boto = document.getElementById('saludar');
#   const resultat = document.getElementById('resultat');
#
#   boto.addEventListener('click', () => {
#     const nom = camp.value;                       // llegeix la casella
#     resultat.textContent = `Hola, ${nom}!`;
#   });
#
# La casella es troba UNA vegada a dalt, i el valor es llegeix DINS de
# l'esdeveniment (perquè ha de ser el valor del moment del clic).
#
# Per als desplegables <select> es llegeix igual amb .value (dóna el
# 'value' de l'opció triada).
#
# PROVA-HO: fes un formulari amb un nom i un botó que escrigui un
# missatge amb el que hi hagis escrit.

# ---------------------------------------------------------------------
# 3.12 Afegir contingut a la pàgina (innerHTML)
# ---------------------------------------------------------------------
# Fins ara hem canviat el text. Per afegir HTML sencer (una llista, una
# fila de taula...) s'utilitza .innerHTML, que interpreta les etiquetes:
#
# HTML:
#   <ul id='llista'></ul>
#
# JS:
#   const llista = document.getElementById('llista');
#   llista.innerHTML = '<li>Pa</li>';           // = substitueix
#   llista.innerHTML += '<li>Llet</li>';        // += afegeix al que ja hi ha
#
#   textContent  -> només text
#   innerHTML    -> text AMB etiquetes HTML
#   =            -> substitueix el contingut
#   +=           -> afegeix al final
#
# PROVA-HO: afegeix 3 elements a una llista des de JS amb +=.

# ---------------------------------------------------------------------
# 3.13 Recorrer un array i pintar-lo a la pàgina (tot junt!)
# ---------------------------------------------------------------------
# Ara combinem el bucle, els objectes i el DOM. Imagina que tens aquestes
# dades i vols fer una taula:
#
# HTML:
#   <table>
#     <tr><th>Nom</th><th>Edat</th></tr>
#     <tbody id='cos'></tbody>
#   </table>
#
# JS:
#   const mascotes = [
#     { nom: 'Lluna', edat: 3 },
#     { nom: 'Rex',   edat: 5 },
#     { nom: 'Nina',  edat: 2 }
#   ];
#
#   const cos = document.getElementById('cos');
#
#   for (const m of mascotes) {
#     cos.innerHTML += `<tr>
#       <td>${m.nom}</td>
#       <td>${m.edat}</td>
#     </tr>`;
#   }
#
# Mira què passa: per cada mascota del array, JS escriu una fila <tr>
# amb les seves dades. Si afegeixes una mascota a l'array, apareix a la
# taula sense tocar l'HTML.
#
# Compara aquest HTML generat amb la taula que vas fer a mà a la 1.10: és
# el mateix, però l'escriu el bucle.
#
# PROVA-HO: fes-ho amb el teu propi array (de pel·lícules, amics...) i la
# teva pròpia taula.

# ---------------------------------------------------------------------
# 3.14 Canviar classes des de JS
# ---------------------------------------------------------------------
# Recorda les classes de la 2.8. JS les pot posar i treure:
#
#   element.classList.add('hi-ha');
#   element.classList.remove('hi-ha');
#   element.classList.toggle('amagat');   // la posa si no hi és, la treu si hi és
#
# Exemple: un botó que amaga i mostra un text.
#
# CSS:
#   .amagat { display: none; }       /* display: none = no es veu */
#
# HTML:
#   <p id='secret'>Text secret</p>
#   <button id='boto'>Mostrar / amagar</button>
#
# JS:
#   const secret = document.getElementById('secret');
#   const boto = document.getElementById('boto');
#
#   boto.addEventListener('click', () => {
#     secret.classList.toggle('amagat');
#   });
#
# Aquest és el patró per canviar l'aspecte segons una condició: JS decideix
# la classe, CSS fa que es vegi diferent.
#
# PROVA-HO: fes el botó de mostrar / amagar.
#
# FINAL DE LA PART 3: ja saps llegir dades d'una pàgina, canviar-la,
# reaccionar a clics i pintar llistes i taules des d'un array. Amb això
# ja pots fer pàgines web amb vida pròpia.


# =====================================================================
# ERRORS TÍPICS (I ON MIRAR)
# =====================================================================
#
#   QUÈ PASSA                        CAUSA PROBABLE
#   -------------------------------  ----------------------------------
#   No veig els canvis               No has desat el fitxer o no has
#                                    refrescat (F5)
#   El CSS no fa res                 Falta la línia <link> al <head>, o
#                                    el nom del fitxer no coincideix
#   El JS no fa res                  Mira la consola (F12): hi haurà un
#                                    error en vermell
#   Cannot read properties of null   getElementById no ha trobat
#                                    l'element: revisa que el id és igual
#   Una cosa surt malament de       Una etiqueta sense tancar (falta el
#   cop a la pàgina                  </...>)
#   El text surt amb ${...} en       Has utilitzat ' ' en lloc d'accents
#   lloc del valor                   oberts ` `
#
# REGLA D'OR: quan alguna cosa no funciona, obre F12 i mira la consola
# abans de res.