
const tbodyManteniments = document.getElementById("tbody_manteniments")

function pintarTaulaManteniments(llista) {

    let fila = ""

    for (manteniment of llista) {

        fila += `<tr>
        <td>${manteniment.DESCRIPCIO}</td>
        <td>${manteniment.COST} €</td>
        <td>${manteniment.DATA_MANTENIMENT}</td>`
    }

    tbodyManteniments.innerHTML = fila
}

async function carregarManteniments() {

    const resposta = await fetch("http://127.0.0.1:8000/manteniments")
    const llistaManteniments = await resposta.json()

    pintarTaulaManteniments(llistaManteniments)

    console.log(llistaManteniments)

    let sumaTotal = 0

    for (manteniment of llistaManteniments) {
        sumaTotal += manteniment.COST
    }

    const pCost = document.getElementById("p_cost")
    pCost.innerText = "Cost total de manteniments = " + sumaTotal + "€"
}

carregarManteniments()