// Bloc 2: Filtrar i cercar (5-6)

// 5. Filtre per estat + cercador per conductor

//  Posa un <select> (Totes / ACTIVA / PENDENT / FINALITZADA) i un <input type="text">
//  per cercar pel nom del conductor. Han de funcionar alhora: si tries "ACTIVA" i
//  escrius "mar", només surten les actives de conductors que comencin per "mar".
//  👉 Pista: un sol if amb les dues condicions unides amb &&, i les dades guardades
//  en una variable fora de la funció (com vehiclesGuardats). Només hi ha una funció
//  que pinta.

// 6. 🆕 Només les d'avui (Date)
//  Afegeix un botó "Només d'avui" que mostri les reserves que comencen avui. Pista:
//  new Date(reserva.DATA_INICI).toDateString() === new Date().toDateString().
//  👉 Compte: a la BD només hi ha dues reserves amb data de novembre del 2026.
//  Crea'n alguna d'avui amb el formulari del 7 per poder-ho provar.

// Bloc 3: Afegir (7-8)
// 7. Formulari d'alta amb desplegables
//  Fes un formulari amb un <select> de vehicles i un altre de conductors (omplerts
//  amb GET /vehicles i GET /conductors), més dos <input type="datetime-local">
//  per a inici i fi. En prémer "Reservar", fes el POST.
//  👉 Que el desplegable mostri la matrícula, però enviï el ID (<option
//  value="${id}">). És la millora respecte al formulari de manteniments, on
//  havies d'escriure l'ID a mà.

// 8. Validar abans d'enviar
//  Abans del fetch, comprova al JS que la data de fi sigui posterior a la d'inici
//  i que no hi hagi camps buits. Si no, mostra un missatge a la pàgina i no enviïs
//  res (return). Quan l'alta surti bé, repinta la taula i buida el formulari.

const tbodyTaulaReserves = document.getElementById('tbody_taula_reserves')
let pMissatgeError = document.getElementById("p_missatge_error")

function formatarData(data) {
    return new Date(data).toLocaleDateString('ca-ES', {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
    })
}

const selectEstatReserva = document.getElementById('select_estat_reserva')

function pintarTaulaReserves(llista) {

    let fila = ""
    let color = "black"

    let pComptadorReserves = document.getElementById("p_comptador_reserves")
    let comptadorActives = 0
    let comptadorFinalitzades = 0
    let comptadorPendents = 0

    const estatEscollit = selectEstatReserva.value

    for (const reserva of llista) {
        if (reserva.ESTAT_RESERVA === "ACTIVA") {
            color = "green"
            comptadorActives += 1
        } else if (reserva.ESTAT_RESERVA === "FINALITZADA") {
            color = "gray"
            comptadorFinalitzades += 1
        } else if (reserva.ESTAT_RESERVA === "PENDENT") {
            color = "orange"
            comptadorPendents += 1
        }

        if (estatEscollit === "Tots" || estatEscollit === reserva.ESTAT_RESERVA) {
            fila += `<tr>
            <td>${reserva.MATRICULA}</td>
            <td>${reserva.NOM}</td>
            <td>${formatarData(reserva.DATA_INICI)}</td>
            <td>${formatarData(reserva.DATA_FI)}</td>
            <td style="color: ${color}">${reserva.ESTAT_RESERVA}</td>
            </tr>`
        }
    }
    tbodyTaulaReserves.innerHTML = fila
    pComptadorReserves.innerHTML = `${comptadorActives} actives - ${comptadorPendents} pendents
                                    - ${comptadorFinalitzades} finalitzades`
}

let reservesGuardades = []
const inputBuscador = document.getElementById('input_buscador')

async function carregarReserves() {

    try {
        const resposta = await fetch("http://127.0.0.1:8000/reserves")
        const dadesReserves = await resposta.json();

        pintarTaulaReserves(dadesReserves);

        reservesGuardades = dadesReserves

    } catch (error) {
        pMissatgeError.innerHTML = "No s'ha pogut connectar amb el servidor.<br>" + error
    }
}

carregarReserves()

selectEstatReserva.addEventListener('change', carregarReserves)

inputBuscador.addEventListener('input', (event) => {

    const inputBuscadorEscrit = inputBuscador.value.toLowerCase()

    const reservesFiltrades = []

    for (const reserva of reservesGuardades) {
        if (inputBuscadorEscrit === "" || reserva.NOM.toLowerCase().startsWith(inputBuscadorEscrit)) {
            reservesFiltrades.push(reserva)
        }
    }
    pintarTaulaReserves(reservesFiltrades)
})

let pReservesAvui = document.getElementById("p_reserves_avui")
const btnReservesAvui = document.getElementById("btn_reserves_avui")

btnReservesAvui.addEventListener("click", () => {

    const reservesAvui = []

    for (const reserva of reservesGuardades) {
        if (new Date(reserva.DATA_INICI).toLocaleDateString() === new Date().toLocaleDateString()) {
            reservesAvui.push(reserva)
        }
    }
    pintarTaulaReserves(reservesAvui)
})

async function omplirSelectFormulari() {

    const respostaVehicles = await fetch("http://127.0.0.1:8000/vehicles")
    const respostaConductors = await fetch("http://127.0.0.1:8000/conductors")
    const llistaVehicles = await respostaVehicles.json();
    const llistaConductors = await respostaConductors.json();

    const selectVehicle = document.getElementById("select_vehicle")
    const selectConductor = document.getElementById("select_conductor")

    let optionVehicle = ""
    let optionConductor = ""

    for (const vehicle of llistaVehicles) {
        optionVehicle += `<option value="${vehicle.VEHICLE_ID}">${vehicle.MATRICULA}</option>`
    }

    for (const conductor of llistaConductors) {
        optionConductor += `<option value="${conductor.CONDUCTOR_ID}">${conductor.NOM}</option>`
    }

    selectVehicle.innerHTML = optionVehicle
    selectConductor.innerHTML = optionConductor
}

omplirSelectFormulari()

const btnReservar = document.getElementById("btn_reservar")
btnReservar.addEventListener("click", registrarReserva)

let pMissatgeErrorFormulari = document.getElementById("p_missatge_error_formulari")

async function registrarReserva() {

    const selectVehicle = document.getElementById("select_vehicle")
    const selectConductor = document.getElementById("select_conductor")
    const inputDataInici = document.getElementById("input_data_inici")
    const inputDataFi = document.getElementById("input_data_fi")
    const selectEstat = document.getElementById("select_estat")

    const vehicleId = selectVehicle.value
    const conductorId = selectConductor.value
    const dataInici = inputDataInici.value
    const dataFi = inputDataFi.value
    const estatReserva = selectEstat.value

    const novaReserva = {
        vehicle_id: Number(vehicleId),
        conductor_id: Number(conductorId),
        data_inici: dataInici,
        data_fi: dataFi,
        estat_reserva: estatReserva
    }

    if (dataFi < dataInici) {
        pMissatgeErrorFormulari.innerHTML = "Les dates no són correctes."
        return
    }

    const resposta = await fetch("http://127.0.0.1:8000/reserves", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(novaReserva)
    })

    if (!resposta.ok) {
        const error = await resposta.json()
        pMissatgeErrorFormulari.innerText = error.detail
    } else {
        const dades = await resposta.json()
        pMissatgeErrorFormulari.innerText = dades.missatge
    }
}

