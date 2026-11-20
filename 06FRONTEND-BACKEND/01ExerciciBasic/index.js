// Bloc 2: Pintar millor (exercicis 4-6)

// Exercici 4: Taula
// Converteix la llista en una <table> amb capçalera (<th>) i columnes: Matrícula,
// Marca, Model, Estat, Quilometratge.

// Exercici 5: Colors per estat
// Posa un color diferent a la cel·la d’estat segons el valor (DISPONIBLE, OCUPAT,
// EN TALLER). Pista: pots posar td.style.color = "green" dins d’un if.

// Exercici 6: Gestionar errors
// Atura la API i recarrega la pàgina. Segurament no passa res i només veus un error
// a la consola. Fes que, si la petició falla, es mostri a la pàgina un missatge
// “No s’ha pogut connectar amb el servidor”.
// 👉 Pista: try { ... } catch (error) { ... }, igual que el que ja fas a Python.

// Bloc 3: Interactuar (exercicis 7-8)
// Exercici 7: Botó de recarregar
// Afegeix un botó “Actualitzar” que torni a carregar la taula. Compte: ha de
// buidar la taula abans de tornar-la a omplir, o es duplicaran les files.

// Exercici 8: Filtrar per estat
// Afegeix un <select> amb les opcions Tots / DISPONIBLE / OCUPAT / EN TALLER.
// Quan canviïs l’opció, la taula només ha de mostrar els vehicles d’aquell estat.
// 👉 Pista: el filtratge el pots fer al frontend, amb un if dins del bucle.
// Ja tens totes les dades.

const selectEstat = document.getElementById('estat_taula')

async function carregarVehicles() {

    try {
        // FEM EL FETCH A VEHICLES I GUARDEM EL RESULTAT EN UNA VARIABLE
        const resposta = await fetch("http://127.0.0.1:8000/vehicles")
        const llistaVehicles = await resposta.json()

        // MOSTREM PER CONSOLA L'ARRAY AMB ELS RESULTATS DEL FETCH
        console.log(llistaVehicles)

        // GUARDEM EN UNA VARIABLE EL <p> ON MOSTREM EL COUNT DE L'ARRAY DE VEHICLES
        const lengthVehicles = document.getElementById('length_vehicles')
        lengthVehicles.textContent = "Hi ha " + llistaVehicles.length + " vehicles en la flota"

        // GUARDEM EN UNA VARIABLE EL <ul>
        const ulVehicles = document.getElementById('llista_vehicles')

        // FEM UN FOREACH QUE RECORRI L'ARRAY AMB ELS RESULTATS D'ABANS
        let li = ""
        for (const vehicle of llistaVehicles) {
            li += `${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL}<br>`

        }
        ulVehicles.innerHTML = li

        const estatEscollit = selectEstat.value
        const tbodyVehicles = document.getElementById('taula_vehicles')
        let files = ""

        for (const vehicle of llistaVehicles) {
            let color = "black"

            if (vehicle.ESTAT === "DISPONIBLE") {
                color = "green"
            } else if (vehicle.ESTAT === "OCUPAT") {
                color = "red"
            } else if (vehicle.ESTAT === "EN TALLER") {
                color = "orange"
            }

            if (estatEscollit === 'Tots' || vehicle.ESTAT === estatEscollit) {
                files += `<tr>
                <td>${vehicle.MATRICULA}</td>
                <td>${vehicle.MARCA}</td>
                <td>${vehicle.MODEL}</td>
                <td style="color: ${color}">${vehicle.ESTAT}</td>
                <td>${vehicle.QUILOMETRATGE}</td>
                </tr>`
            }

        }
        tbodyVehicles.innerHTML = files

    } catch (error) {
        let missatge = document.getElementById('missatge_error')
        missatge.innerHTML = "No s'ha pogut connectar amb el servidor.<br>" + error
    }
}

// CRIDEM LA FUNCIÓ
carregarVehicles()

const btnRefrescar = document.getElementById('btn_refrescar')
btnRefrescar.addEventListener('click', carregarVehicles)

selectEstat.addEventListener('change', carregarVehicles)