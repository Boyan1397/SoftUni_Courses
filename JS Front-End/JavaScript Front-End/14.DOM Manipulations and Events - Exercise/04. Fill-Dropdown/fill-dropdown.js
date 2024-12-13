document.addEventListener('DOMContentLoaded', solve);

function solve() {
    let buttonElement = document.querySelector('input[type="submit"]')

    buttonElement.addEventListener('click', (e) => {
        e.preventDefault()
        let textElement = document.getElementById('newItemText');
        let valueElement = document.getElementById('newItemValue');
        let selectElement = document.getElementById('menu')

        if (textElement.value === '' || valueElement.value === '') return

        let optionElement = document.createElement('option')
        optionElement.textContent = textElement.value
        optionElement.value = valueElement.value

        selectElement.append(optionElement)
        
        textElement.value = ''
        valueElement.value = ''
    })
}