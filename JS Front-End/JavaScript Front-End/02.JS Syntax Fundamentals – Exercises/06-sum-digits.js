function solve(number) {
    let sum = 0
    let strNumber = number.toString()
    
    for (let i = 0; i < strNumber.length; i++) {
        sum += Number(strNumber[i])
        // sum += Number(strNumber.charAt(i))
    }
    console.log(sum);
    
}

solve(245678)

// mathematical
// function solve(number) {
//     let sum = 0;
//     while (number > 0) {
//         sum += (number % 10);
//         number = Math.trunc(number / 10)
//     }
//     console.log(sum);
    
// }

