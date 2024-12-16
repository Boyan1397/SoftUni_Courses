// A Promise is an object that represents the eventual 
// completion or failure of an asynchronous operation.
// It allows you to handle tasks that might take time 
// (like data fetching or waiting for a timeout) in a structured way.

// Promise creating
const fishing = new Promise((resolve, reject) => {
    if (0.3 < Math.random()) {
        return reject('No fishes catched today')
    }
    
    setTimeout(() => {
        resolve('YEYY WE GOT FISH FOR DINNER')
    }, 3000);
})

fishing.then(message => {
    console.log((message));
})
.catch(message => {
    console.log(message);
})
.finally(message => console.log('It is what it is'))

// same usage promise with shorter syntax
// const weddingPromise = Promise()
const vacationPromiseNew = new Promise((resolve) => {
    resolve('Good we are going')
})

vacationPromiseNew.then(message => {
    console.log(message)
})

const vacationPromise = Promise.resolve('Good we are going 2')
vacationPromise.then((message) => console.log(message))

// multiple promise in one promise all()

let createPromise = function(message, time) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(message)
        }, time);
    })
}

let promiseGroup = Promise.all([
    Promise.resolve('first message'),
    createPromise('creating second', 2000),
    createPromise('creating third', 3000)
])

promiseGroup
    .then((values) => console.log(values))
