function focused() {
    let inputElements = document.querySelectorAll('div > input')
    
    inputElements.forEach(input => {
        input.addEventListener('focus', (e) => {
            e.currentTarget.parentNode.classList.add('focused')
        })

        input.addEventListener('blur', (e) => {
            e.currentTarget.parentNode.classList.remove('focused')
        })  
    })   
}