function addItem() {
    let itemsElement = document.getElementById('items')
    let inputElement = document.querySelector('input:nth-of-type(1)')
    let buttonElement = document.querySelector('input:nth-of-type(2)')   
    let input = inputElement.value

    let listItemElement = document.createElement('li');
    listItemElement.textContent = input

    let deleteLinkElement = document.createElement('a')
    deleteLinkElement.textContent = '[Delete]'
    deleteLinkElement.href = '#'
    listItemElement.appendChild(deleteLinkElement)
    
    itemsElement.appendChild(listItemElement)

    inputElement.value = ''

    deleteLinkElement.addEventListener('click', (e) => {
        e.currentTarget.parentElement.remove()
    })
}