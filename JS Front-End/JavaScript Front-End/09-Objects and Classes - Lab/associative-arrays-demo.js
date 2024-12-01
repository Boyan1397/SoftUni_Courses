// its just an object all same type value data
let fullName = 'Bobo Ivanov'

let englishDictionary = {
    'Antonia Ivanova': '087831232',
    'Nikola Ivanov': '082131231',
    'Petur Nikolov': '082131235',
    [fullName]: '0821312344'
}

englishDictionary['Simona Trendafilova'] = '082131236'
englishDictionary.Bobkata = '082131236'

console.log(englishDictionary);

// FOR IN (The objects are not iterable and bcs of that we use FOR IN loop to loop thourgh objects) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// It loops only though KEYS

for (let key in englishDictionary) {
    console.log(key); 
}

console.log(englishDictionary);

// delete from object
delete englishDictionary.Bobkata
console.log(englishDictionary);

// check if KEY is in object or IN
if (englishDictionary.hasOwnProperty('Nikola Ivanov')) {
    console.log('Nikola Ivanov is found');
} else {
    console.log('not found');
    
}

// check if VALUE is in object
if (englishDictionary['Nikola Ivanov']) {
    console.log('match');
} else {
    console.log('not match');
    
}


// sorting objects 
// by keys
let sorted = Object
    .entries(englishDictionary)
    .sort((a, b) => a[0].localeCompare(b[0]));

sorted = Object.fromEntries(sorted)

console.log(sorted);

// by values
let sortedD = Object
    .entries(englishDictionary)
    .sort((a, b) => a[1].localeCompare(b[1]));

sortedD = Object.fromEntries(sortedD)

console.log(sortedD);

// WE DO IT BY BOTH ONLY IF WE HAVE IDENTICAL VALUES

let obj = {a: 'Hi', b: 'Hello'}
const {a, b} = obj
console.log(a);
