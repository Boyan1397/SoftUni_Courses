function solve(first, second, third) {
    let sum = (a, b) => a + b;
    let substract = ((a, b) => a - b)

    let result = substract(sum(first, second), third)
    console.log(result);
}

solve(23, 6, 10)


// DUMB ONE
// function sumOfFirstTwo(a, b) {
//     return a + b
// }

// function subtract(sum, c) {
//     return sum - c
// }

// function solve(a, b, c) {
//     let sum = sumOfFirstTwo(a, b)
//     let result = subtract(sum, c)
//     return result
// }


// console.log(solve(23, 6, 10));



