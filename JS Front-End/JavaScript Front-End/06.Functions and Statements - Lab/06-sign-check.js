function solve(num1, num2, num3) {
    let multiply = (a, b) => a * b

    if (multiply(multiply(num1, num2), num3) < 0) {
        console.log('Negative');
    } else {
        console.log('Positive');
        
    }
}



// DUMB ONE
// function solve(num1, num2, num3) {
//     let negativesCounter = 0
//     let numbers = Array(num1, num2, num3)
//     numbers.forEach(num => {
//         if (num < 0) {
//             negativesCounter += 1
//         }
//     });
//     if (negativesCounter % 2 == 0) {
//         console.log('Positive');
//     } else {
//         console.log('Negative');
        
//     } 
// }

solve(5, 12, -15)
solve(-5, -12, 15)
solve(-5, -12, -15)