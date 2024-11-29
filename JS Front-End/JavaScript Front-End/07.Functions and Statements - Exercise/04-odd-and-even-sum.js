function getSum(number, filter) {
    number = number.toString()
    number = number
    .split('')
    .map(Number)
    .filter(filter) 
    //      x => x % 2 !== 0
    
    return number.reduce((sum, num) => sum + num, 0)
}

function solve(number) {
    let oddSum = getSum(number, x => x % 2 !== 0)
    let evenSum = getSum(number, x => x % 2 === 0)

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}

console.log(solve(1000435));
console.log(solve(3495892137259234));



// function solve(number) {
//     let numberArr = makeArray(number) 
//     let [oddSum, evenSum] = getSums(numberArr)

//     function makeArray(number) {
//         number = number.toString()
//         number = number
//         .split('')
//         .map(Number)

//         return number
//     }
    
//     function getSums(numberArr) {
//         let oddSum = 0
//         let evenSum = 0
//         for (let num of numberArr) {
//             if (num % 2 !== 0) {
//                 oddSum += num
//             } else {
//                 evenSum += num
//             }
//         }
//         return [oddSum, evenSum]
//     }

//     console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
// }




