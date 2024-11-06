// function cookByNumbers(number, ...operations) {
//     let myNumber = Number(number)

//     for (let operation of operations) {
//         switch (operation) {
//             case 'chop':
//                 myNumber /= 2;
//                 console.log(myNumber);
//                 break;
//             case 'chop':
//                 myNumber /= 2;
//                 console.log(myNumber);
//                 break;
//             case 'dice':
//                 myNumber = Math.sqrt(myNumber);
//                 console.log(myNumber);
//                 break;
//             case 'spice':
//                 myNumber += 1;
//                 console.log(myNumber);
//                 break;
//             case 'bake':
//                 myNumber *= 3;
//                 console.log(myNumber);
//                 break;
//             case 'fillet':
//                 myNumber -= (myNumber * 0.2);
//                 console.log(myNumber);

//         }

//     }
// }
function cookByNumbers(number, ...operations) {
    let myNumber = Number(number)

    for (let operation of operations) {
        if (operation === 'chop') {
            myNumber /= 2;
            console.log(myNumber);
        } else if (operation === 'dice') {
            myNumber = Math.sqrt(myNumber);
            console.log(myNumber);
        } else if (operation === 'spice') {
            myNumber += 1;
            console.log(myNumber);
        } else if (operation === 'bake') {
            myNumber *= 3;
            console.log(myNumber);
        } else if (operation === 'fillet') {
            myNumber -= (myNumber * 0.2);
            console.log(myNumber);
        }
    }
}

cookByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cookByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet')
