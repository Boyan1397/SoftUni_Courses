// HTML Targeting by Tag and Class Names –
let myId = document.getElementById('example')
setTimeout(() => myId.textContent = 'Georgi me uhapa', 2000)

let classList = document.getElementsByClassName('averages')
console.dir(classList[0].textContent);

let paragraphs = document.getElementsByTagName('p')
console.dir(paragraphs);

// Targeting with CSS Selectors
let selectorElement = document.querySelector('#Lora')
console.dir(selectorElement);

let selectorsEls = document.querySelectorAll('.tonis')
console.dir(selectorsEls);

let selectorLast = document.querySelectorAll('div > p')
console.log(selectorLast);

let selectorType = document.querySelector('input[type=text]')
selectorType.value = 'Nikola Bonev'
// console.log(selectorType.value);


// NodeList vs. HTMLCollection

// NodeList can be iterated with foreach (gets all elements) its static
// static NodeList 
let staticNodeList = document.querySelectorAll('#special > *')
console.log(staticNodeList);
staticNodeList.forEach(element => console.log(element))

// live NodeList like that it (gets all nodes even like those text ones)
let liveNodeList = document.querySelector('#special')
liveNodeList = liveNodeList.childNodes
console.log(liveNodeList[0]);

// HTML collection
//HTML collection have to be converted to array and then can be iterated with foreach (gets all elements)
let htmlsCollection = document.getElementById('special')
htmlsCollection = htmlsCollection.children
console.log(htmlsCollection);



// iterate
for (let element of htmlsCollection) {
    console.log(element);
}




