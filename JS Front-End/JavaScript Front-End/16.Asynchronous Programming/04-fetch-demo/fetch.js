// get with server (GET)
let booksUrl = 'http://localhost:3030/jsonstore/books'
// fetch(booksUrl)
//     .then((response) => response.json())
//     .then(data => console.log(data))
//     .catch(err => console.log(err))


// create book (POST)
// fetch(booksUrl, {
//     method: 'POST',
//     headers: {
//         'content-type': 'application/json'
//     },
//     body: JSON.stringify({
//         title: 'Narnia',
//         Author: 'Papazov'
//     })
// })
//     .then((response) => response.json())
//     .then((data) => console.log(data))
//     .catch(err => console.log(err))


// fetch(booksUrl, {
//     method: 'POST',
//     headers: {
//         'content-type': 'application/json'
//     },
//     body: JSON.stringify({
//         title: 'PODIGOTO',
//         Author: 'Vazov'
//     })
// })
//     .then((response) => response.json())
//     .then((data) => console.log(data))
//     .catch(err => console.log(err))

// edit book PUT

// fetch(`${booksUrl}/949c3971-d93f-4b46-9a81-503aefe9bcd1`, {
//     method: 'PUT',
//     headers: {
//         'content-type': 'application/json'
//     },
//     body: JSON.stringify({
//         "title": "The Chronicles of Narnia",
//         "Author": "Papazov",
//         "_id": "949c3971-d93f-4b46-9a81-503aefe9bcd1"
//     })
// })
//     .then((response) => response.json())
//     .then((data) => console.log(data))
//     .catch(err => err)

// delete book


// fetch(`${booksUrl}/53f0e956-acc5-4c7b-ad7e-ac66c6041dd6`, {
//     method: 'DELETE'
// })
//     .then(res => console.log(res))
//     .catch(err => console.log(err))