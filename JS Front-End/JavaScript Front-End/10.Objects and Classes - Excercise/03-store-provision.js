function solve(stockArr, ordersArr) {
    storeData = {}
    for (let i = 0; i < stockArr.length; i += 2) {
        storeData[stockArr[i]] = Number(stockArr[i + 1])
    }

    for (let i = 0; i < ordersArr.length; i += 2) {
        if (storeData[ordersArr[i]]) {
            storeData[ordersArr[i]] += Number(ordersArr[i + 1])
        } else {
            storeData[ordersArr[i]] = Number(ordersArr[i + 1])
        }
    }
    
    for (let product in storeData) {
        console.log(`${product} -> ${storeData[product]}`);
    }
    
}

solve([ 'Chips', '5', 'CocaCola', '9', 'Bananas',
         '14', 'Pasta', '4', 'Beer', '2' ],

        [ 'Flour', '44', 'Oil', '12', 'Pasta',
         '7', 'Tomatoes', '70', 'Bananas', '30' ])