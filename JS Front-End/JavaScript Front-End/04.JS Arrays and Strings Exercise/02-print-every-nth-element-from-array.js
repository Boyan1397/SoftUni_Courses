// function getNthElements(stringsArr, step) {
//     let result = []
//     for (i = 0; i < stringsArr.length; i += step)
//         result.push(stringsArr[i])

//     return result
// }

// console.log(getNthElements(['5', '20', '31', '4', '20'], 2));
// console.log(getNthElements(['dsa', 'asd', 'test', 'tset'], 2));
// console.log(getNthElements(['1', '2', '3', '4', '5'], 6));


function getNthElementss(stringsArr, step) {
    let result = stringsArr.filter((element, index) => !(index % step))
    return result
}


console.log(getNthElementss(['5', '20', '31', '4', '20'], 2));
console.log(getNthElementss(['dsa', 'asd', 'test', 'tset'], 2));
console.log(getNthElementss(['1', '2', '3', '4', '5'], 6));


// function getNthElement(stringsArr, step) {
//     let elementsArr = []
//     for (let i = 0;i < stringsArr.length; i++) {
//         if (i % step === 0) {
//             elementsArr.push(stringsArr[i])
//         }
//     }

//     return elementsArr
// }

// console.log(getNthElement(['5', '20', '31', '4', '20'], 2));
// console.log(getNthElement(['dsa', 'asd', 'test', 'tset'], 2));
// console.log(getNthElement(['1', '2', '3', '4', '5'], 6));

