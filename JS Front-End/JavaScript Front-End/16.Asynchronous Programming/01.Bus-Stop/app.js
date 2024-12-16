function getInfo() {
    let inputStopIdEl = document.getElementById('stopId')
    let stopNameResultEl = document.getElementById('stopName')
    let busesResultsUl = document.getElementById('buses')

    let inputId = inputStopIdEl.value
    
    let url = 'http://localhost:3030/jsonstore/bus/businfo'

    fetch(`${url}/${inputId}`)
        .then(response => response.json())
        .then((data) => {
            let myStation = data.name
            stopNameResultEl.textContent = myStation

            for (let bus in data.buses) {
                let createBusLiElement = document.createElement('li')
                createBusLiElement.textContent = `Bus ${bus} arrives in ${data.buses['bus']} minutes`
                busesResultsUl.appendChild(createBusLiElement)
            }
        })
        .catch(() => stopNameResultEl.textContent = 'Error')
}