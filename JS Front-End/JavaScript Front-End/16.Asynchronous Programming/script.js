
let url = 'https://swapi.py4e.com/api/'

fetch(`${url}/people/1`)
    .then((response) => {
        return response.json()
    })
    .then((data) => console.log(data))

    .catch((err) => console.log('Error has occurred'))


fetch(`${url}/people/2`)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.log('There was an error, sorry'))