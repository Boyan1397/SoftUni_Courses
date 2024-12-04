let carOne = {brand: 'Mercedes', fuel: 'Diesel', engine: '2.2 Litres'}
console.log(carOne);

console.log(carOne.brand);
console.log(carOne['fuel']);
console.log(carOne.engine);

carOne.warranty = '2 Years'
console.log(carOne.warranty);
console.log(carOne);

// Adding dynamically (when we want to assign key or value from a variable)
car2 = {}
let hpKey = 'Horse Power';
car2[hpKey] = '333'
// 
console.log(car2);
car2.Brand = 'Audi'
console.log(car2);


// Adding dynamically in the literal

let rangeKey = 'range'
let car3 = {[rangeKey]: 500}
console.log(car3);

