function solve(number) {
    let isSame = true;
    let sum = 0;

    let strNumber = number.toString()
    for (let i = 0; i < strNumber.length; i++) {
        sum += Number(strNumber[i]);
        if (strNumber[0] !== strNumber[i]) {
            isSame = false;
        }
    }
    console.log(isSame);  
    console.log(sum);
    
}

solve(1234)


// Mathematical!
// function solve(number) {
//     let lastDigit = number % 10;  // Get the last digit to use as a reference
//     let isSame = true;
//     let sum = 0;

//     while (number > 0) {
//         let currentDigit = number % 10; // Extract the last digit
//         sum += currentDigit;

//         if (currentDigit !== lastDigit) {
//             isSame = false; // Set to false if any digit is different
//         }
        
//         number = Math.floor(number / 10); // Remove the last digit
//     }

//     console.log(isSame);
//     console.log(sum);
// }

// // Example usage:
// solve(1234)


// DONT LIKE IT
// function solve(number) {
//     let strNumber = number.toString()
//     let isSame = true;
//     let currentNum = 0
//     let sum = Number(strNumber[currentNum]);

//     for (let i = 1; i < strNumber.length; i++) {
//         sum += Number(strNumber[i]);
//         if (strNumber[currentNum] !== strNumber[i]) {
//             isSame = false;
//             currentNum += 1
//         }
//     }
//     console.log(isSame);
//     console.log(sum);
    
    
// }


