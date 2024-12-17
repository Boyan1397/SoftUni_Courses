function attachEvents() {
    let loadButtonElement = document.getElementById('btnLoad')
    let createButtonElement = document.getElementById('btnCreate')
    // delete button
    let inputPersonElement = document.getElementById('person')
    let inputPhoneElement = document.getElementById('phone')
    let phonebookElement = document.getElementById('phonebook')

    let baseUrl = 'http://localhost:3030/jsonstore/phonebook'

    loadButtonElement.addEventListener('click', () => {
        phonebookElement.innerHTML = ''
        fetch(baseUrl)
            .then(response => response.json())
            .then(data => {
                Object.values(data).forEach(info => createLiElement(info))
            })
    })

    createButtonElement.addEventListener('click', () => {
        
        let person = inputPersonElement.value;
        let phone = inputPhoneElement.value

        inputPersonElement.value = ''
        inputPhoneElement.value = ''
        
        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({person, phone})
        })
        .then(response => response.json())
        .then(data => {
            createLiElement(data)
        })
    })


    function createLiElement(info) {
        let newLiElement = document.createElement('li')
        newLiElement.textContent = `${info.person}: ${info.phone}`
        let newDeleteButton = document.createElement('button')
        newDeleteButton.textContent = 'Delete'
        newLiElement.appendChild(newDeleteButton)
        phonebookElement.appendChild(newLiElement)

        newDeleteButton.addEventListener('click', () => {
            fetch(baseUrl + `/${info._id}`, {
                method: 'DELETE'
            })
            .then(response => response.json())
            .then(data => {
                newLiElement.remove()
            })
        })
    }
}

attachEvents();