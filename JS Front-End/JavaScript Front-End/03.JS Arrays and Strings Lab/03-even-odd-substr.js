function subtractOddEvenWithReduce(numbersArr) {
    let result = numbersArr.reduce((sum, num) => num % 2 === 0 ? sum + num : sum - num ,0)
    return result
}

console.log(subtractOddEvenWithReduce([1,2,3,4,5,6]));
console.log(subtractOddEvenWithReduce([3,5,7,9]));


// function subtractOddEven(numbersArr) {
//     let evens = 0;
//     let odds = 0;
//     let result = 0;
//     numbersArr.forEach(num => {
//         if (num % 2 === 0) {
//             evens += num
//         } else {odds += num}
//     });
//     result = evens - odds
//     return result
// }

// console.log(subtractOddEven([1,2,3,4,5,6]));
// console.log(subtractOddEven([3,5,7,9]));



// function subtractOddEven(numbersArr) {
//     let evens = numbersArr.filter(num => num % 2 === 0).reduce((evenSum, evenCurrent) => evenSum + evenCurrent, 0)
//     let odds = numbersArr.filter(num => num % 2 !== 0).reduce((oddSum, oddCurrent) => oddSum + oddCurrent, 0)
//     const result = evens - odds
    
//     return result
// }


// with reduce only
