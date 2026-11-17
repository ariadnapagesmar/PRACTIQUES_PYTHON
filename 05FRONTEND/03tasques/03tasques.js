// JavaScript (lliçons 3.1 a 3.14)
//
// Exercici 15: Les dades a la consola
//
// Connecta tasques.js. Crea un array de 4 objectes, cada un amb text, prioritat
// ('alta', 'mitjana' o 'baixa') i feta (true o false). Fes una funció
// comptarPendents() que recorri l’array i retorni quantes tasques tenen feta
// a false. Escriu el resultat a la consola amb un text amb accents oberts.
// Lliçons 3.2, 3.3, 3.5, 3.6, 3.7 i 3.8.
// Pista: dins de la funció necessitaràs una variable que comenci a 0 (amb let)
// i que vagi pujant dins del bucle amb un if.
// Has de veure: a la consola, «Tasques pendents: 3» (o el nombre que sigui).
//
// Exercici 16: Pintar la llista des de JS
//
// Crea un nou <ul> en l'HTML i fes una funció pintarLlista() que recorri l’array i
// escrigui un <li> per tasca, amb la classe de la seva prioritat. Si la tasca
// està feta, que el <li> tingui també la classe feta (classes separades per
// un espai: class="alta feta"). Crida la funció una vegada al final.
// Lliçons 3.5, 3.12, 3.13 i 3.14.
// Pista: per ajuntar les classes pensa en una variable que comenci amb la prioritat,
// i a la qual afegeixes ' feta' només si cal.
// Has de veure: la mateixa llista de l’exercici 12, però generada pel JS.
//
// Exercici 17: Afegir una tasca nova
//
// Fes que el botó «Afegir» llegeixi el text i la prioritat del formulari, creï
// un objecte nou amb feta: false, l’afegeixi a l’array i torni a pintar la llista.
// Lliçons 3.6, 3.8, 3.10, 3.11 i 3.12.
// Pista: si repintes amb += sense buidar abans, les tasques es dupliquen. Mira
// la diferència entre = i += de la 3.12 i decideix on has de posar un
// innerHTML = '' a la funció.
// Has de veure: la tasca nova apareix al final de la llista, amb el seu color.
//
// Exercici 18: Validar abans d’afegir
//
// Millora el botó: si el camp de text està buit, no afegeixis res i escriu un
// missatge d’error al #missatge. Si està bé, afegeix la tasca i buida el missatge.
// Lliçons 3.4 i 3.11.
// Pista: compara el valor amb === i un text buit ''. Pensa que el return dins
// d’una funció també serveix per sortir abans.
// Has de veure: error en vermell si prems «Afegir» amb la caixa buida, i res
// d’error si l’omples.
//
// Exercici 19: El comptador viu
//
// Afegeix al HTML un <p> buit i fes que mostri sempre «Pendents: X de Y», on X
// és el resultat de la funció de l’exercici 15 i Y el total de tasques. Ha
// d’actualitzar-se cada vegada que repintes la llista.
// Lliçons 3.3, 3.5 i 3.6.
// Pista: no cal crear cap funció nova. Pensa on dins de pintarLlista() has de
// posar la línia perquè s’executi sempre.
// Has de veure: el comptador puja quan afegeixes una tasca.
//
// Exercici 20: Completar-ho tot i mode fosc
//
// Afegeix dos botons nous. El primer, «Completar totes», fa que totes les
// tasques passin a feta = true i es torni a pintar la llista (amb el comptador
// a 0). El segon, «Mode fosc», fa canviar entre un aspecte clar i un de fosc:
// crea una classe .fosc al CSS (fons negre i lletra blanca) i posa-la o treu-la
// del <body> a cada clic.
// Lliçons 3.9, 3.10 i 3.14.
// Pista: el <body> també pot tenir un id perquè el trobis amb getElementById.
// Has de veure: totes les tasques es ratllen d’un clic, i el mode fosc va i ve
// cada vegada que premes el botó.

const tasques = [
    {tasca: 'Revisió mèdica anual', prioritat: 'mitjana', feta: false},
    {tasca: 'Vacunar al gat', prioritat: 'alta', feta: true},
    {tasca: 'Ficar la rentadora', prioritat: 'baixa', feta: false},
    {tasca: 'Visita amb el psicòleg', prioritat: 'mitjana', feta: true}
]

function comptarPendents(array_tasques) {
    let comptador_false = 0
    for (const tasca of array_tasques) {
        if (tasca.feta == false) {
            comptador_false += 1
        }
    }

    return console.log('Total de tasques sense completar: ' + comptador_false)
}

comptarPendents(tasques)

const llistaPintar = document.getElementById('pintar_llista')

function pintarLlista(array_tasques) {
    llistaPintar.innerHTML = ''
    for (const tasca of array_tasques) {
        let prioritat = tasca.prioritat
        if (tasca.feta == true) {
            prioritat += " feta"
            llistaPintar.innerHTML += `<li class="${prioritat}">${tasca.tasca}</li>`
        } else {
            llistaPintar.innerHTML += `<li class="${prioritat}">${tasca.tasca}</li>`
        }
    }
}

// Exercici 17: Afegir una tasca nova
//
// Fes que el botó «Afegir» llegeixi el text i la prioritat del formulari, creï
// un objecte nou amb feta: false, l’afegeixi a l’array i torni a pintar la llista.
// Lliçons 3.6, 3.8, 3.10, 3.11 i 3.12.
// Pista: si repintes amb += sense buidar abans, les tasques es dupliquen. Mira
// la diferència entre = i += de la 3.12 i decideix on has de posar un
// innerHTML = '' a la funció.
// Has de veure: la tasca nova apareix al final de la llista, amb el seu color.

const botoAfegir = document.getElementById('btn_afegir')
const tascaAfegir = document.getElementById('nova_tasca')
const prioritatAfegir = document.getElementById('prioritat')

botoAfegir.addEventListener('click', () => {
    const novaTasca = tascaAfegir.value
    const novaPrioritat = prioritatAfegir.value
    tasques.push({tasca: novaTasca, prioritat: novaPrioritat, feta: false})
    pintarLlista(tasques)
})

pintarLlista(tasques)