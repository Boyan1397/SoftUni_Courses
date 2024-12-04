let car = {brand: 'Mercedes', model: 'GLE 350DE', horsepower: '333'}

// convert from OBJECT to JSON data string
let data = JSON.stringify(car, null, 2)
console.log(data);

// convert from JSON to object 
let originalCar = JSON.parse(data)
console.log(originalCar.brand);

