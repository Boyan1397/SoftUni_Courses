function attachEvents() {
    let buttonElement = document.getElementById('submit')
    let firstNameElement = document.querySelector('.inputs > input[name="firstName"]')
    let lastNameElement = document.querySelector('.inputs > input[name="lastName"]')
    let facultyNumberElement = document.querySelector('.inputs > input[name="facultyNumber"]')
    let gradeElement = document.querySelector('.inputs > input[name="grade"]')
    let tbodyElement = document.querySelector('tbody')

    let baseUrl = 'http://localhost:3030/jsonstore/collections/students'

    fetch(baseUrl)
        .then(response => response.json())
        .then(data => {
            let dataObj = Object.values(data)
            dataObj.forEach(friend => {createNewRow(friend)})
        })

    buttonElement.addEventListener('click', () => {       

        let bodyObj = {
                firstName: firstNameElement.value,
                lastName:lastNameElement.value,
                facultyNumber: facultyNumberElement.value,
                grade: gradeElement.value
            };

        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(bodyObj)
        })
        .then(response => response.json())
        .then(data => {
            createNewRow(data)
        })

        firstNameElement.value= ''
        lastNameElement.value = ''
        facultyNumberElement.value = ''
        gradeElement.value = ''
    })

    function createNewRow(friend) {
        let createTr = document.createElement('tr')
                let createFirstNameTd = document.createElement('td')
                let createLastNameTd = document.createElement('td')
                let createFacultyTd = document.createElement('td')
                let createGradeTd = document.createElement('td')

                createFirstNameTd.textContent = friend.firstName
                createLastNameTd.textContent = friend.lastName
                createFacultyTd.textContent = friend.facultyNumber
                createGradeTd.textContent = friend.grade
                
                createTr.appendChild(createFirstNameTd)
                createTr.appendChild(createLastNameTd)
                createTr.appendChild(createFacultyTd)
                createTr.appendChild(createGradeTd) 
                tbodyElement.appendChild(createTr)
    } 
}

attachEvents();
