let loadButton = document.getElementById('load-orders')
let editOrderButton = document.getElementById('edit-order')
let orderButton = document.getElementById('order-btn')
let elementsList = document.getElementById('list')

let inputNameElement = document.getElementById('name')
let inputQuantityElement = document.getElementById('quantity')
let inputDateElement = document.getElementById('date')

let currentOrderId = null;

// !
let baseUrl = 'http://localhost:3030/jsonstore/orders'

// !!
loadButton.addEventListener('click', loadOrders)
orderButton.addEventListener('click', (e) => {
    e.preventDefault()
    createElement()
})
editOrderButton.addEventListener('click', (e) => {
    e.preventDefault()
    editOrder()
})

async function loadOrders() {
    let response = await fetch(baseUrl)
    let data = await response.json()

    elementsList.innerHTML = ''

    for (let order of Object.values(data)) {
        let name = order.name
        let quantity = order.quantity
        let date = order.date
        // container and h-s
        let newContainerDiv = document.createElement('div')
        newContainerDiv.classList.add('container')

        let newNameH2 = document.createElement('h2')
        newNameH2.textContent = name

        let newDateH3 = document.createElement('h3')
        newDateH3.textContent = date

        let newQuantityH3 = document.createElement('h3')
        newQuantityH3.textContent = quantity
        // buttons
        let newChangeButton = document.createElement('button')
        newChangeButton.classList.add('change-btn')
        newChangeButton.textContent = 'Change'

        let newDoneButton = document.createElement('button')
        newDoneButton.classList.add('done-btn')
        newDoneButton.textContent = 'Done'
        // appendchildren
        newContainerDiv.appendChild(newNameH2)
        newContainerDiv.appendChild(newDateH3)
        newContainerDiv.appendChild(newQuantityH3)
        newContainerDiv.appendChild(newChangeButton)
        newContainerDiv.appendChild(newDoneButton)
        elementsList.appendChild(newContainerDiv)

        editOrderButton.disabled = true

        newChangeButton.addEventListener('click', () => {
            currentOrderId = order._id
            newContainerDiv.remove()
            inputNameElement.value = order.name
            inputQuantityElement.value = order.quantity
            inputDateElement.value = order.date
            editOrderButton.disabled = false
            orderButton.disabled = true
        })

        newDoneButton.addEventListener('click', async () => {
            let response = await fetch(`${baseUrl}/${order._id}`, {
                method: 'DELETE'
            })

            loadOrders()

        })
    }
    
}

async function createElement() {
    let name = inputNameElement.value
    let quantity = inputQuantityElement.value
    let date = inputDateElement.value
    let objBody = {name, quantity, date}

    let response = await fetch(baseUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(objBody)
    })
    
    inputNameElement.value = ''
    inputQuantityElement.value = ''
    inputDateElement.value = ''

    loadOrders()
}

async function editOrder() {
    let name = inputNameElement.value
    let quantity = inputQuantityElement.value
    let date = inputDateElement.value
    let objBody = {name, quantity, date, _id: currentOrderId}

    let response = await fetch(`${baseUrl}/${currentOrderId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(objBody)
    })

    editOrderButton.disabled = true
    orderButton.disabled = false
    currentOrderId = null
    loadOrders()

}