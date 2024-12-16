// Async with callback func

exampleFunc(() => console.log('example')) 
console.log('start');
delayedFunction(() => console.log('Delayed message'))
console.log('finish');

function exampleFunc(callback) {
    callback()
}

function delayedFunction(callback) {
    setTimeout(() => { callback()     
    }, 3000);
}
