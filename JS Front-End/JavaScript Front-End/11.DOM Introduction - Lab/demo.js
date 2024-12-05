// HTML COLLECTION ADDING LIVE
// let listItemsCollection = document.getElementById('listItems')
// let li = document.createElement('li')
// li.textContent = 'Added content'
// listItemsCollection.appendChild(li)

// iterate (We make it live iterable when we use children)
// listItemsCollection = listItemsCollection.children
// for (let item of listItemsCollection) {
//     console.log(item.textContent);
// }

// listItemsCollection[0].style.color = 'red'


// NodeList
// let nodesList = document.querySelectorAll('#listItems > li')
// nodesList.forEach(element => console.log(element))



let listItems = document.getElementById('listItems')
let li = document.createElement('li')
li.textContent = 'Some data'
listItems.appendChild(li)
console.log(listItems);
