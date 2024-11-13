let cars = ['BMW', 'AUDI', 'MERCEDES', 'TOYOTA']
console.log(cars);


// add last item
cars.push('HONDA')
console.log(cars);


// get and remove last item
cars.pop() 
console.log(cars);

// remove first item
firstCar = cars.shift()
console.log(firstCar);
console.log(cars);

// add first item 
cars.unshift('MITSUBISHI')
console.log(cars);

// remove with splice
cars.splice(1, 2)
console.log(cars);

// add with splice
cars.splice(1, 0, 'MERCEDES', 'AUDI')
console.log(cars);

// reverse array 
cars.reverse()
console.log(cars);

// join
let strCars = cars.join(', ')
console.log(strCars);


// slice
let slicedCars = cars.slice(1, 3)
console.log(slicedCars);

let slicedCar = cars.slice(2,3)
console.log(slicedCar);


// check is element INCLUDES - true or false
console.log(cars.includes('AUDI'));

// returns the index by the value of the element
console.log(cars.indexOf('MITSUBISHI'));
console.log(cars.indexOf('Vw')); 


// returns the element if its in

let carElement = cars.find(car => car === 'AUDI')
console.log(carElement);

// Find all indexes
let topCars = ['TOYOTA', 'BMW', 'MERCEDES', 'TOYOTA']

let tIndex = topCars.indexOf('TOYOTA');
while (tIndex >= 0) {
    console.log(tIndex);
    tIndex = topCars.indexOf('TOYOTA', tIndex + 1)
 }

//  forEach funtion
// LOOPING THROUGH THE ARRAY printing, summing, counting and little things like that !!!
let sum = 0
someNums = [4, 3, 5, 3, 66]
someNums.forEach(number =>  sum += number)
console.log(sum);


// mapping
// CREATING NEW ARRAY and modifying the elements in it !!! AND THE ELEMENTS ARE THE SAME COUNT
let numbers = [1, 2, 4, 5, 3]
let newNumbers = numbers.map(number => number += 1)
console.log(newNumbers);


// filter
let oddNumbers = numbers.filter(num => num % 2 !== 0);
console.log(oddNumbers);


// reduce
let someNumbers = [1, 2, 4, 5, 3]
const totalPrice = someNumbers.reduce((sum, currentPrice) => {
    return sum + currentPrice
}, 0)

console.log(totalPrice);



// STRING METHODS

// indexOf
let myString = 'I am JavaScript developer'
javaIdx = myString.indexOf('Java')
console.log(javaIdx);


// extracting substring
let mySubstring = myString.substring(javaIdx, 9)
console.log(mySubstring);

// replace
let pythonDev = myString.replace('JavaScript', 'Python')
console.log(pythonDev);
// replaceAll possible


// split making a array of a string
let pythonArray = pythonDev.split(' ')
console.log(pythonArray);


// paddStart

let padTest = "I am testing the pad"
console.log(padTest.padStart(167, '0'));

let textTwo = 'a33'
console.log(textTwo.padStart(8, '0'));

let text = "010";
console.log(text.padStart(8, '0')); 


// reversing a string
myString = 'I am JavaScript developer'
reversedString = myString.split('').reverse().join('')
console.log(reversedString);
