// Bloc B: Variacions de la taula (4-6)

// 4. Taula petita
//  Fes una taula amb només dues columnes: Matrícula i Quilometratge.

// 5. Quilometratge alt
//  Pinta el quilometratge en vermell si és més gran de 50000.

// 6. Comptar vehicles en taller
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

// GUARDEN EN UNA VARIABLE EL BODY DE LA TAULA DE VEHICLES, PERÒ FORA DE LA FUNCIÓ
// PER PODER FER-LA SERVIR FORA DE LA FUNCIÓ
const tbodyVehicles = document.getElementById('tbody_vehicles')
let missatgeError = document.getElementById('missatge_error')

// CREEM LA FUNCIÓ QUE ESCRIU ELS VEHICLES DINS DE LA TAULA
function pintarTaulaVehicles(llista) {
    // CREEM LA VARIABLE 'FILA' AMB UN STRING BUIT, AQUÍ GUARDAREM CADA FILA DE
    // LA TAULA I EL QUE VOLEM ESCRIURE EN ELLA
    let fila = ""
    // UN FOREACH EN LA LLISTA AMB ELS VEHICLES, QUE RECORRI CADA VEHICLE
    for (const vehicle of llista) {
        // DE BASE ESTÀ TOT ESCRIT DE COLOR NEGRE
        let color = "black"
        // SI EL QUILOMETRATGE SUPERA ELS 50000KM, EL PINTEM DE COLOR VERMELL
        if (vehicle.QUILOMETRATGE > 50000) {
            color = "red"
        }

        // GUARDEM EN 'FILA' CADA FILERA I CASELLA QUE VOLEM ESCRIURE EN LA TAULA
        fila += `<tr>
        <td>${vehicle.MATRICULA}</td>
        <td>${vehicle.MARCA}</td>
        <td style="color: ${color}">${vehicle.QUILOMETRATGE}</td>
        </tr>`
    }
    // GUARDEM LA FILA DINS DEL BODY DE LA TAULA
    tbodyVehicles.innerHTML = fila
}

// CREEM UNA VARIABLE LLISTA ON GUARDAREM ELS RESULTATS DEL FETCH A VEHICLES
let vehiclesGuardats = []

// CREEM UNA VARIABLE AGAFANT L'INPUT DEL FORMULARI DE L'HTML
const input = document.getElementById('input_taula')

// FORA DE LA FUNCIÓ, PERQUÈ NOMÉS ES CREÏ UN LISTENER QUAN ES CARREGA LA PÀGINA,
// FEM EL LISTENER EN L'INPUT
input.addEventListener('input', () => {
    // GUARDEM EL QUE ESCRIGUI L'USUARI DINS DE L'INPUT EN UN ALTRE VARIABLE
    const inputTaula = input.value.toLowerCase()
    // CREEM UNA VARIABLE LLISTA QUE SERVIRÀ PER GUARDAR ELS RESULTATS DE LA CERCA
    // DE L'INPUT EN LA TAULA, MOSTRANT NOMÉS ELS VEHICLES ON LA MARCA SIGUI IGUAL
    // AL QUE HAGI ESCRIT L'USUARI A L'INPUT
    const vehiclesFiltrats = []

    // UN FOREACH A LA LLISTA ON EM GUARDAT ELS RESULTATS DEL FETCH AMB TOTS ELS VEHICLES
    for (const vehicle of vehiclesGuardats) {
        // UN IF ON NOMÉS AFEGIREM A LA NOVA LLISTA AMB ELS VEHICLES FILTRATS, ELS
        // VEHICLES QUE COINCIDEIX AMB LA CONDICIÓ (EL QUE ESCRIGUI L'USUARI A L'INPUT)
        if (inputTaula === "" || vehicle.MARCA.toLowerCase().startsWith(inputTaula)) {
            // FEM UN PUSH (COM L'APPEND) A AQUESTA LLISTA NOVA
            vehiclesFiltrats.push(vehicle)
        }
    }
    // CRIDEM LA FUNCIÓ QUE PINTA LA TAULA, PERÒ AMB ELS NOUS FILTRES QUE EM FICAT
    pintarTaulaVehicles(vehiclesFiltrats)
})

// FEM LA FUNCIÓ QUE SERVEIX PRINCIPALMENT PER FER EL FETCH A LA BD PER BUSCAR LA
// RUTA GET I CARREGAR ELS VEHICLES
async function carregarVehicles() {

    try {
        // UNA VARIABLE AMB LA RESPOSTA AL FETCH
        const resposta = await fetch("http://127.0.0.1:8000/vehicles")
        // UN ALTRE VARIABLE ON GUARDEM EN FORMAT JSON LA RESPOSTA
        const vehicles = await resposta.json()
        // GUARDEM EN LA VARIABLE D'ABANS LA LLISTA AMB ELS VEHICLES, PER PODER FER-LA
        // SERVIR FORA D'AQUESTA FUNCIÓ TAMBÉ
        vehiclesGuardats = vehicles

        // DOS COMPTADORS PER MOSTRAR ELS VEHICLES DISPONIBLES I EN TALLER
        let comptador_disponibles = 0
        let comptador_taller = 0

        // UN FOREACH QUE RECORRI CADA VEHICLE DE LA BD
        for (const vehicle of vehicles) {
            // PER CONSOLA ELS MOSTREM TOTS UN SOTA L'ALTRE
            console.log(`${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL}`)

            // SUMEM U AL COMPTADOR DE VEHICLES DISPONIBLES PER CADA VEHICLE AMB L'ESTAT
            // 'DISPONIBLE' I FEM EL MATEIX AMB 'EN TALLER'
            if (vehicle.ESTAT === 'DISPONIBLE') {
                comptador_disponibles += 1
            }
            if (vehicle.ESTAT === 'EN TALLER') {
                comptador_taller += 1
            }
        }

        // MOSTREM EN UN <p> D'HTML ELS RESULTATS DELS COMPTADORS
        const pVehiclesDisponibles = document.getElementById('p_vehicles_disponibles')
        pVehiclesDisponibles.innerHTML = `Hi ha ${comptador_disponibles} vehicles 
                                            disponibles de ${vehicles.length}`;
        const pVehiclesTaller = document.getElementById('p_vehicles_taller')
        pVehiclesTaller.innerHTML = `Hi ha ${comptador_taller} vehicles en el 
                                        taller de ${vehicles.length}`

        // GUARDEM EN UNA VARIABLE EL UL DE L'HTML ON MOSTRAREM EN FORMAT LLISTA NOMÉS
        // ELS VEHICLES OCUPATS
        const ulVehiclesOcupats = document.getElementById('ul_vehicles_ocupats')
        // CREEM UNA VARIABLE BUIDA ON GUARDAREM EL QUE ESCRIUREM EN CADA <li>
        let li = ""
        // PER CADA VEHICLE EN LA LLISTA...
        for (const vehicle of vehicles) {
            // ... SI L'ESTAT ÉS 'OCUPAT'
            if (vehicle.ESTAT === 'OCUPAT') {
                // QUE IMPRIMEIXI LA INFORMACIÓ DELS VEHICLES EN QÜESTIÓ I HO GUARDI
                // EN LA VARIABLE AMB ELS LI
                li += `-   ${vehicle.MATRICULA} - ${vehicle.MARCA} ${vehicle.MODEL} - ${vehicle.ESTAT}<br>`
            }
        }
        // GUARDEM DINS DEL <ul> TOTS ELS <li> AMB ELS VEHICLES OCUPATS
        ulVehiclesOcupats.innerHTML = li

        // CRIDEM LA FUNCIÓ QUE PINTA LA TAULA I LI PASSEM LA LLISTA AMB ELS VEHICLES
        // DEL FETCH PERQUÈ LA TINGUI TAMBÉ I LA PUGUI FER SERVIR
        pintarTaulaVehicles(vehicles)

        // VARIABLE QUE AGAFA EL PARÀGRAF ON MOSTRAREM L'HORA DE L'ÚLTIM COP QUE S'HA
        // REFRESCAT LA PÀGINA
        const pData = document.getElementById('p_data')
        // MOSTREM L'HORA QUE SIGUI QUAN REFRESQUIS LA PÀGINA
        pData.innerHTML = "Última actualització: " + new Date().toLocaleTimeString()
    } catch (error) {
        missatgeError.innerHTML = "No s'ha pogut connectar amb el servidor.<br>" + error
    }


}

// CRIDEM LA FUNCIÓ QUE FA EL FETCH PERQUÈ TOT COMENCI A FUNCIONAR
carregarVehicles()

// Bloc D: Un endpoint nou (10)

// 10. Conductors (detallet nou: repetir el CRUD a l'inrevés)
//  Al backend, fes un GET /conductors (igual que el de vehicles, amb la
//  taula CONDUCTORS). Al frontend, pinta'ls en una segona taula amb Nom, Carnet
//  i Telèfon.
//  👉 Aquí practiques les dues bandes alhora, que és el que et falta per sentir-te
//  còmoda.

const tbodyConductors = document.getElementById('tbody_conductors')

function pintarTaulaConductors(llista) {

    let fila = ""

    for (const conductor of llista) {
        fila += `<tr>
        <td>${conductor.NOM}</td>
        <td>${conductor.CARNET}</td>
        <td>${conductor.TELEFON}</td>
        </tr>`
    }

    tbodyConductors.innerHTML = fila
}

async function carregarConductors() {

    try {
        const resposta = await fetch("http://127.0.0.1:8000/conductors")
        const conductors = await resposta.json()

        pintarTaulaConductors(conductors)
    } catch (error) {
        missatgeError.innerHTML = "No s'ha pogut connectar amb el servidor.<br>" + error
    }
}

carregarConductors()