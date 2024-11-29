// BETTER
function solve(a, b, operator) {
    const operators = {
        multiply: (a, b) => a * b,
        divide: (a, b) => a / b,
        add: (a, b) => a + b,
        subtract: (a, b) => a - b
    }

    return operators[operator](a, b)
}

console.log(solve(5, 5, 'multiply'));


// function solve(a, b, operator) {
//     function getOperator(operator) {
//         switch (operator) {
//             case 'multiply':
//             return (a, b) => a * b;
    
//             case 'divide':
//             return (a, b) => a / b
    
//             case 'add':
//             return (a, b) => a + b
    
//             case 'subtract':
//             return (a, b) => a - b
//         }
//     }

//     let myOperatorFunc = getOperator(operator)
//     console.log(myOperatorFunc(a, b));  
// }

// solve(5, 5, 'multiply')