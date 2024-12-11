function addItem() {
    // find where you need to add it
    let itemsListElement = document.querySelector('#items')
     // get input element
    let inputElement = document.getElementById('newItemText')

    // create new item
    let newListItemElement = document.createElement('li')
    // set its texcontent or etc...
    newListItemElement.textContent = inputElement.value

    // insert it
    itemsListElement.appendChild(newListItemElement)

    inputElement.value = ''

    console.log('TODO:...');
}