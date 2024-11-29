// FUNCTIONAL!
function returnResult(product, quantity) {

    let price = getPrice(product)
    let result = (price * quantity).toFixed(2)
    console.log(result);

    function getPrice(product) {
        switch (product) {
            case 'water':
                return 1;
            case 'coffee':
                return 1.50;
            case 'coke':
                return 1.40;
            case 'snacks':
                return 2.00;
        }
    }
}

returnResult('water', 3)

// WITH OBJECT!
// function getTotal(product, quantity) {

//     let products = {
//         coffee: 1.50,
//         water: 1.00,
//         coke: 1.40,
//         snacks: 2.00
//     }

//     let result = (products[product] * quantity).toFixed(2)
//     return result
    
// }

// console.log(getTotal("water", 5));


