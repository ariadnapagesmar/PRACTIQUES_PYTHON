
// Bloc 2: Buscar per vehicle (5-7)

// 5. 🐍🌐 Manteniments d'un vehicle
//  Al backend, fes GET /manteniments/{vehicle_id}, que retorni només els d'aquell
//  vehicle (un WHERE). Al frontend, afegeix un <input type="number"> i un botó
//  "Cercar" que cridi aquesta ruta.
//  👉 Ja has fet rutes amb {matricula}. Aquí el nou és construir la URL al fetch
//  amb el valor de l'input.

// 6. 🐍🌐 Amb la matrícula (🆕 JOIN)
//  Ara a la taula surt un número de vehicle, que no diu res. Al backend, modifica
//  la consulta amb un JOIN a VEHICLES perquè també retorni MATRICULA i MARCA, i
//  mostra-les a la taula.

// 7. 🐍🌐 Vehicle sense manteniments (🆕 resposta.ok)
//  Si el vehicle no té manteniments, el backend ha de respondre amb un 404 i un
//  missatge. Al frontend, comprova resposta.ok abans de fer .json() i, si no ho és,
//  mostra el missatge d'error a la pàgina.
//  👉 Prova-ho amb el vehicle 4, que no en té.

// Bloc 3: Afegir dades (8-10)

// 8. 🐍 Alta de manteniment (només backend)
//  Fes POST /manteniments amb un model Pydantic (vehicle_id, descripció, cost,
//  data), igual que el que ja fas per als vehicles. Prova'l des de la documentació
//  automàtica de FastAPI (http://127.0.0.1:8000/docs), sense frontend.
//  👉 Pensa què passa si el vehicle_id no existeix: la BD té una clau forana. Fes
//  que l'API respongui amb un error clar.

// 9. 🌐 Formulari d'alta (🆕 fetch amb POST)
//  Fes un formulari amb vehicle, descripció, cost i data, i envia'l al POST del 8.
//  De moment, mostra per consola què et respon l'API.

// 10. 🐍🌐 Alta completa
//  Quan l'alta surti bé, mostra el missatge que retorna l'API i actualitza la
//  taula sense recarregar la pàgina. Si hi ha un error (per exemple, un vehicle
//  inexistent), mostra el que digui el backend, no un text inventat al frontend.

const tbodyManteniments = document.getElementById("tbody_manteniments")
const pMissatgeError = document.getElementById("p_missatge_error")

function pintarTaulaManteniments(llista) {

    let fila = ""

    for (const manteniment of llista) {

        fila += `<tr>
        <td>${manteniment.DESCRIPCIO}</td>
        <td>${manteniment.COST} €</td>
        <td>${manteniment.DATA_MANTENIMENT}</td>
        <td>${manteniment.MATRICULA}</td>
        <td>${manteniment.MARCA}</td>
        </tr>`
    }

    tbodyManteniments.innerHTML = fila
}

async function carregarManteniments() {

    try {
        const resposta = await fetch("http://127.0.0.1:8000/manteniments")
        const llistaManteniments = await resposta.json()

        pintarTaulaManteniments(llistaManteniments)

        console.log(llistaManteniments)

        let sumaTotal = 0
        let mesCar = ["", 0]

        for (const manteniment of llistaManteniments) {
            sumaTotal += manteniment.COST
            if (manteniment.COST > mesCar[1]) {
                mesCar = [manteniment.DESCRIPCIO, manteniment.COST]
            }
        }

        const pCost = document.getElementById("p_cost")
        pCost.innerText = "Cost total de manteniments = " + sumaTotal.toFixed(2) + "€"
        const pMesCar  = document.getElementById("p_mes_car")
        pMesCar.innerText = "Manteniment més car = " + mesCar[0] + " - " + mesCar[1]
    } catch (error) {
        pMissatgeError.innerText = "No s'ha pogut connectar amb el servidor.<br>" + error
    }
}

carregarManteniments()

const btnCercar = document.getElementById("btn_cercar")
btnCercar.addEventListener("click", cercarManteniment)

async function cercarManteniment() {

    try {
        const inputCercar = document.getElementById("input_cercar").value
        const pMantenimentCercat = document.getElementById("p_manteniment_cercat")

        const resposta = await fetch(`http://127.0.0.1:8000/manteniments/${inputCercar}`)

        if (!resposta.ok) {
            const error = await resposta.json()

            pMantenimentCercat.innerHTML = error.detail
        } else {
            const mantenimentCercat = await resposta.json()

            let fila = ""
            for (const manteniment of mantenimentCercat) {
                fila += manteniment.VEHICLE_ID + " - " + manteniment.DESCRIPCIO + " - " +
                    manteniment.COST + "€ - " + manteniment.DATA_MANTENIMENT + "\n"
            }
            pMantenimentCercat.innerText = fila
        }
    } catch (error) {
        pMissatgeError.innerText = "No s'ha pogut connectar al servidor.<br>" + error
    }
}

const btnAfegirManteniment = document.getElementById("btn_afegir_manteniment")
btnAfegirManteniment.addEventListener("click", registrarManteniment)

async function registrarManteniment() {

    const inputVehicleId = document.getElementById("input_vehicle_id")
    const inputDescripcio = document.getElementById("input_descripcio")
    const inputCost = document.getElementById("input_cost")
    const inputDataManteniment = document.getElementById("input_data_manteniment")

    const vehicleIdNou = inputVehicleId.value
    const descripcioNova = inputDescripcio.value
    const costNou = inputCost.value
    const dataMantenimentNova = inputDataManteniment.value

    const nouManteniment = {
        vehicle_id: Number(vehicleIdNou),
        descripcio: descripcioNova,
        cost: Number(costNou),
        data_manteniment: dataMantenimentNova
    }

    try {
        const resposta = await fetch("http://127.0.0.1:8000/manteniments", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(nouManteniment)
        })

        let pMissatgeAfegir = document.getElementById("p_missatge_afegir")

        if (!resposta.ok) {
            const error = await resposta.json()
            console.log("Error: ", error.detail)
            pMissatgeAfegir.innerText = error.detail
        } else {
            const dades = await resposta.json()
            console.log(dades.missatge)
            pMissatgeAfegir.innerText = dades.missatge
            await carregarManteniments()
        }
    } catch (error) {
        pMissatgeError.innerText = "No s'ha pogut connectar al servidor.<br>" + error
    }
}

