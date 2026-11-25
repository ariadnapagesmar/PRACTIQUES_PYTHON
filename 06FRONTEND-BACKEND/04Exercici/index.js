


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

function pintarTaulaReserves(llista) {

    let fila = ""

    for (const reserva of llista) {

        fila += `<tr>
        <td>${reserva.MATRICULA}</td>
        <td>${reserva.NOM}</td>
        <td>${formatarData(reserva.DATA_INICI)}</td>
        <td>${formatarData(reserva.DATA_FI)}</td>
        <td>${reserva.ESTAT_RESERVA}</td>
        </tr>`
    }
    tbodyTaulaReserves.innerHTML = fila
}

async function carregarReserves() {

    try {
        const resposta = await fetch("http://127.0.0.1:8000/reserves")
        const dadesReserves = await resposta.json();

        pintarTaulaReserves(dadesReserves);

    } catch (error) {
        pMissatgeError.innerHTML = "No s'ha pogut connectar amb el servidor.<br>" + error
    }
}

carregarReserves()