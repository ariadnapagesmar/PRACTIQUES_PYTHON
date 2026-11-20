// Bloc B: Variacions de la taula (4-6)

// 4. Taula petita
//  Fes una taula amb només dues columnes: Matrícula i Quilometratge.

// 5. Quilometratge alt
//  Pinta el quilometratge en vermell si és més gran de 50000.

// 6. Taula buida
//  Mostra en un <p> el text: “Hi ha X vehicles en taller”.

// Bloc C: Més interacció (7-9)

// 7. Cercador per marca (detallet nou: input)
//  Afegeix un <input type="text">. Mentre l'usuari escriu, la taula mostra només
//  els vehicles de la marca escrita. Pista: l'esdeveniment és 'input' en lloc
//  de 'change', i .toLowerCase() et ajuda a no distingir majúscules.

// 8. Hora d'actualització (detallet nou: Date)
//  Després de cada refresc, mostra "Última actualització: hh:mm:ss".
//  Pista: new Date().toLocaleTimeString().

// 9. Separar en funcions
//  Deixa carregarVehicles() només per demanar les dades i crea pintarTaula(llista),
//  que rep la llista com a paràmetre i pinta. És el que vam veure amb
//  pintarNumVehicles.

async function carregarVehicles() {

    const resposta = await fetch("http://127.0.0.1:8000/vehicles")
    const vehicles = await resposta.json()

    let comptador_disponibles = 0
    let comptador_taller = 0

    for (const vehicle of vehicles) {
        console.log(`${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL}`)

        if (vehicle.ESTAT === 'DISPONIBLE') {
            comptador_disponibles += 1
        }

        if (vehicle.ESTAT === 'EN TALLER') {
            comptador_taller += 1
        }
    }

    const pVehiclesDisponibles = document.getElementById('p_vehicles_disponibles')
    pVehiclesDisponibles.innerHTML = `Hi ha ${comptador_disponibles} vehicles 
                                        disponibles de ${vehicles.length}`;

    const pVehiclesTaller = document.getElementById('p_vehicles_taller')
    pVehiclesTaller.innerHTML = `Hi ha ${comptador_taller} vehicles en el 
                                    taller de ${vehicles.length}`

    const ulVehiclesOcupats = document.getElementById('ul_vehicles_ocupats')
    let li = ""
    for (const vehicle of vehicles) {
        if (vehicle.ESTAT === 'OCUPAT') {
            li += `-   ${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL} - ${vehicle.ESTAT}<br>`
        }
    }
    ulVehiclesOcupats.innerHTML = li

    const tbodyVehicles = document.getElementById('tbody_vehicles')
    let fila = ""
    for (const vehicle of vehicles) {
        let color = "black"

        if (vehicle.QUILOMETRATGE > 50000) {
            color = "red"
        }

        fila += `<tr>
        <td>${vehicle.MATRICULA}</td>
        <td>${vehicle.MARCA}</td>
        <td style="color: ${color}">${vehicle.QUILOMETRATGE}</td>
        </tr>`
    }
    tbodyVehicles.innerHTML = fila

    // const input = document.getElementById('input_taula')
    // const inputTaula = input.value.toLowerCase()
    // let filaFiltrada = ""
    // inputTaula.addEventListener('input', () => {
    //     for (const vehicle of vehicles) {
    //         let color = "black"
    //
    //
    //         if (vehicle.QUILOMETRATGE > 50000) {
    //             color = "red"
    //         }
    //
    //         if (vehicle.MARCA.toLowerCase() === inputTaula.toLowerCase()) {
    //             filaFiltrada += `<tr>
    //             <td>${vehicle.MATRICULA}</td>
    //             <td>${vehicle.MARCA}</td>
    //             <td style="color: ${color}">${vehicle.QUILOMETRATGE}</td>
    //             </tr>`
    //         }
    //
    //     }
    //     tbodyVehicles.innerHTML = filaFiltrada
    // })
}

carregarVehicles()