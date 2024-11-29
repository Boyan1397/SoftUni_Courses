function executeExpression(operatorFunc, num1, num2) {
    let result = operatorFunc(num1, num2)
    return (`The result of the task is ${result}`)
}

// function declaration
function multiply(numOne, numTwo) {
    return numOne * numTwo
}

console.log(executeExpression(multiply, 2, 6));

// function expression body in as argument
console.log(executeExpression(function(numOne, numTwo) {
    return numOne / numTwo
}, 18, 3));


// arrow function
console.log(executeExpression((a, b) => a + b, 50, 60))


// returning a function


function loggerBuilder(date) {
    return function textGiver(text) {
        console.log(`${date} ${text}`);
    }
}

let logger = loggerBuilder('11.04.2003')
logger('Lora')

