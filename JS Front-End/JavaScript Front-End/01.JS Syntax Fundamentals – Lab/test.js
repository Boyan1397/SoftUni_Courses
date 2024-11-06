// Variables
let a = 15
let b = 15

console.log(a + b);

const pi = 3.14

// if, else if, else
if (a < b) {
    console.log('A smaller than B')
} else if (a > b) {
    console.log('A bigger than B');
} else {
    console.log('equal');
}

// Functions
function add(first, second) {  // Function declaration
    console.log(first + second)
}

add(2, pi) // Function calling

// String concatenation
console.log('First answer is '+ b);

// String interpolation
console.log(`The answer is ${a - b}`);

// Changing decimal and making it a string
console.log(pi.toFixed(5));

// Switch

const favAnimal = 'Lion'

switch (favAnimal) {
    case 'cat':
        break;

    case 'Lion':
        console.log('That is a lion');
        
        break;
}

// Logical operators 
let temperature = 3

// && and
if (temperature > 0 && temperature <= 30) {
    console.log("Temp is good");
} else {
    console.log("Temp is bad");  
}

// || or
if (temperature < 5 || temperature > 35) {
    console.log("BAAD");  
}

if (temperature != 15) {
    console.log("not 15");
}

// ! not
let isSunny = false 

if (!isSunny) {
    console.log("Its cloudy");
} else {
    console.log("Its nikola");
}

isSunny = !isSunny 
console.log(isSunny);

// truthy and falsy

let isBobo = true
if (isBobo) {
    console.log("ITS TRUEE");
}

// Loops

for (let i = 10; i > 0; i--) {
    if (i % 2 !== 0)
    console.log(i);
}

// let i = 1

// while (i <= 8) {
//     console.log(i)
//     i++   
// }

console.log(typeof (i))

