// JavaScript (lliçons 3.1 a 3.14)

// Exercici 7: JS a la consola

// Crea app.js, connecta'l i, sense tocar la pàgina, fes: un array amb 4 objectes
// (títol i any), un bucle que escrigui cada títol a la consola, i un if que
// escrigui «clàssica» o «moderna» segons l'any.
// Lliçons 3.1 a 3.8.
// Pista: obre la consola amb F12. Tot el resultat l'has de veure allà.

// Exercici 8: El primer clic

// Afegeix un botó i un paràgraf a la pàgina. Quan es prem el botó, el paràgraf
// mostra un missatge (per exemple, el nombre de pel·lícules de l'array).
// Lliçons 3.9 i 3.10.
// Pista: dos passos: troba els elements amb getElementById i després escolta el
// clic amb addEventListener. Si no passa res, mira F12.

// Exercici 9: Llegir el formulari

// Fes que el botó «Afegir» de l'exercici 4 llegeixi el títol que hi ha escrit i
// el mostri en un paràgraf (només això, sense afegir res a la taula).
// Lliçó 3.11.
// Pista: .value es llegeix dins de l'esdeveniment, no abans.

// Exercici 10: Pintar la taula des de JS

// Deixa el <tbody> de la taula buit i fes que sigui el JS qui l'ompli, amb un
// bucle sobre l'array de l'exercici 7. Que cada fila porti la classe
// (.clàssica o .moderna) segons l'any.
// Lliçons 3.12 a 3.14.
// Pista: dins del bucle, un += a innerHTML amb una plantilla amb accents oberts.
// Compara el que ha generat JS amb la taula que vas fer a mà a l'exercici 3:
// ha de quedar igual.

const pelicules = [
    {titol: 'The Texas Chain Saw Massacre', any: 1974},
    {titol: 'Toy Story 2', any: 1999},
    {titol: 'Avengers: Endgame', any: 2019},
    {titol: 'A Silent Voice', any: 2016}
]

for (const pelicula of pelicules) {
    if (pelicula.any > 2000) {
        console.log(pelicula.titol + ' - ' + pelicula.any + ' -> Moderna')
    } else {
        console.log(pelicula.titol + ' - ' + pelicula.any + ' -> Clàssica')
    }
}

let missatge = document.getElementById('missatge')
const botoGenerar = document.getElementById('generar')

botoGenerar.addEventListener('click', () => {
    missatge.textContent = 'Has fet clic!'
})