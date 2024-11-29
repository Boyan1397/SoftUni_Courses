function solve(num) {
    for (let i = 0; i < num; i++) {
        console.log(createRow(num));  
    }
}

function createRow(num) {
    let rowNums = Array(num).fill(num).join(' ');
    return rowNums
}

solve(3)
solve(7)
solve(2)

// function solve(number) {
//     let numbersMatrix = []
//     for (let i = 0; i < number; i++) {
//         let row = []
//         for (let i = 0; i < number; i++) {
//             row.push(number)
//         }
//         numbersMatrix.push(row)
//     }
//     numbersMatrix.forEach(numArr => {
//         console.log(numArr.join(' '));
//     });
// }

// solve(3)
// solve(7)
// solve(2)