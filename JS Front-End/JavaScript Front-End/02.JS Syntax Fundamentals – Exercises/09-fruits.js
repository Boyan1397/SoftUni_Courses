function solve(fruit, grams, price) {
    let gramsToKilos = grams / 1000
    let totalPrice = price * gramsToKilos
    console.log(`I need $${(totalPrice).toFixed(2)} to buy ${gramsToKilos.toFixed(2)} kilograms ${fruit}.`);
    
}

solve('orange', 2500, 1.80)