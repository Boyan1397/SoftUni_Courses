function solve(count, groupType, day) {
    let price;
    switch (day) {
        case ('Friday'):
            switch (groupType) {
                case ('Students'):
                    price = 8.45 * count
                    break;
                case ('Business'):
                    price = 10.90 
                    break;
                case ('Regular'):
                    price = 15 * count
                    break;
            }
            break;
        
        case ('Saturday'):
            switch (groupType) {
                case ('Students'):
                    price = 9.80 * count
                    break;
                case ('Business'):
                    price = 15.60 
                    break;
                case ('Regular'):
                    price = 20 * count
                    break;
            }
            break;
        
        case ('Sunday'):
            switch (groupType) {
                case ('Students'):
                    price = 10.46 * count
                    break;
                case ('Business'):
                    price = 16 
                    break;
                case ('Regular'):
                    price = 22.50 * count
                    break;
            }
            break;
    }

    let finalPrice;

    if (groupType === 'Students') {
        if (count >= 30) {
            finalPrice = price - (price * 0.15)
        } else {
            finalPrice = price
        }
    } else if (groupType === 'Business') {
        if (count >= 100) {
            finalPrice = (count - 10) * price
        } else {
            finalPrice = count * price
        }
    } else if (groupType === 'Regular') {
        if (10 <= count && count <= 20) {
            finalPrice = price - (price * 0.05)
        } else {
            finalPrice = price
        }
    }

    console.log(`Total price: ${finalPrice.toFixed(2)}`)
}

solve(30, "Students", "Sunday")
solve(40, "Regular", "Saturday")

// function solve(count, groupType, day) {
//     let price;
//     switch (day) {
//         case ('Friday'):
//             switch (groupType) {
//                 case ('Students'):
//                     price = count * 8.45;
//                     if (count >= 30) {
//                         price = price - (price * 0.15);
//                     }
//                     break;
//                 case ('Business'):
//                     if (count >= 100) {
//                         price = (count - 10) * 10.90
//                     } else {
//                         price = count * 10.90;        
//                     }
//                     break;
//                 case ('Regular'):
//                     price = count * 15;
//                     if (10 <= count && count <= 20) {
//                         price -= (price * 0.05)
//                     }
//                     break;
//             }
//             break;
//         case ('Saturday'):
//             switch (groupType) {
//                 case ('Students'):
//                     price = count * 9.80;
//                     if (count >= 30) {
//                         price = price - (price * 0.15);
//                     }
//                     break;
//                 case ('Business'):
//                     if (count >= 100) {
//                         price = (count - 10) * 15.60;
//                     } else {
//                         price = count * 15.60;        
//                     }
//                     break;
//                 case ('Regular'):
//                     price = count * 20;
//                     if (10 <= count && count <= 20) {
//                         price -= (price * 0.05)
//                     }
//                     break;
//             }
//             break;
        
//         case ('Sunday'):
//             switch (groupType) {
//                 case ('Students'):
//                     price = count * 10.46;
//                     if (count >= 30) {
//                         price = price - (price * 0.15);
//                     }
//                     break;
//                 case ('Business'):
//                     if (count >= 100) {
//                         price = (count - 10) * 16;
//                     } else {
//                         price = count * 16;        
//                     }
//                     break;
//                 case ('Regular'):
//                     price = count * 22.50;
//                     if (10 <= count && count <= 20) {
//                         price -= (price * 0.05)
//                     }
//                     break;
//             }
//             break;
//     }

//     console.log(`Total price: ${price.toFixed(2)}`)
// }
