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

async function carregarVehicles() {

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
    for (const vehicle of llistaVehicles) {
        // CREEM UN ELEMENT <li> PER CADA VEHICLE (CADA TOMB QUE FA EL BUCLE)
        const li = document.createElement('li')
        // ESCRIVIM DINS DEL <li> LA MATRICULA, MARCA I MODEL QUE VOLEM MOSTRAR
        li.textContent = `${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL}`
        // FEM UN .appendChild(li) AL <ul> PER A QUE S'AFEGEIXIN A LA LLISTA DEL HTML
        ulVehicles.appendChild(li)
    }

    const tbodyVehicles = document.getElementById('taula_vehicles')
    let files = ""

    for (const vehicle of llistaVehicles) {
        files += `<tr>
            <td>${vehicle.MATRICULA}</td>
            <td>${vehicle.MARCA}</td>
            <td>${vehicle.MODEL}</td>
            <td>${vehicle.ESTAT}</td>
            <td>${vehicle.QUILOMETRATGE}</td>
            </tr>`
    }
    tbodyVehicles.innerHTML = files

}

// CRIDEM LA FUNCIÓ
carregarVehicles()


