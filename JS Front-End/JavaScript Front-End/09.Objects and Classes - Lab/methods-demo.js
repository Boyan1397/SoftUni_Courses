// function methods
let parrot = {
    parrotName: 'Kiko',
    age: 17,
    breed: 'Jako',
    sound: function() {
        console.log('KraKra')
    },
    sleep: () => console.log('zzzzz...'),
    talk: () => console.log('Im TaLking'),
    
    
}

let callSound = 'sound'

console.log(parrot);
parrot.sound()
parrot['sound']()
parrot[callSound]()
parrot.sleep()
parrot.talk()

// adding methods
let dog = {}
dog.bark = () => console.log('af af'),
dog.bark()

// method notation
let cat = {
    owner: 'Boni',
    catSound() {
        console.log('Mql');
        
    }
}

// putting in outside function
function snore(time) {
    console.log('grrgrgrgrgrgrgrgrgrgrgrgrgrgrgrg');
    console.log(time);   
}

let dad = {
    dadName: 'Stancho',
    snore,
}

dad.snore(15)


console.log(cat);

cat.catSound()

// built in methods

let allKeys = Object.keys(parrot)
console.log(allKeys);


let allValues = Object.values(parrot)
console.log(allValues);

// get kvps
let allKvps = Object.entries(parrot)
console.log(allKvps);
allKvps.forEach(kvp => {
    console.log(kvp);
    
});

// make kvps to object again
let originalObject = Object.fromEntries(allKvps)
console.log(originalObject);

