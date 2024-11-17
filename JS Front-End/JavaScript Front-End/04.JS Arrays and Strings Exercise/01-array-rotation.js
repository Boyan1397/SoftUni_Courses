function numbersRotation(numbersArr, rotations) {
    for (let i = 0; i < rotations; i++) {
        let firstElement = numbersArr.shift()
        numbersArr.push(firstElement)
    }
    
    return numbersArr.join(' ')
}

console.log(numbersRotation([51, 47, 32, 61, 21], 2));
console.log(numbersRotation([32, 21, 61, 1]));
console.log(numbersRotation([2, 4, 15, 31], 5));

// DUMB SOLUTION
// function numbersRotation(numbersArr, rotations) {
//     for (i = 0; i < rotations; i++) {
//         let rotatedArr = []
//         for (j = 0; j < numbersArr.length; j++) {
//             rotatedArr[j] = numbersArr[j + 1]
//         }
//         rotatedArr[rotatedArr.length - 1] = numbersArr[0]
//         numbersArr = rotatedArr
//     }

//     return numbersArr.join(' ')
// }
//                          [47, ]
// console.log(numbersRotation([51, 47, 32, 61, 21], 2));
// console.log(numbersRotation([32, 21, 61, 1]));
// console.log(numbersRotation([2, 4, 15, 31], 5));

