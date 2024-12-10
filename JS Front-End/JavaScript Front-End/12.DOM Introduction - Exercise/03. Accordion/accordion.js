function toggle() {
    let buttonElement = document.querySelector('.head > .button')
    let extraElement = document.getElementById('extra')
    
    let button = buttonElement.textContent 

    if (button === 'More') {
        extraElement.style.display = 'block'
        buttonElement.textContent = 'Less'
    } else if (button === 'Less') {
        extraElement.style.display = 'none'
        buttonElement.textContent = 'More'
    }
}