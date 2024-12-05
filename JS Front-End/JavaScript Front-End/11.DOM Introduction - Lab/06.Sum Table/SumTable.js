// function sumTable() {
//     const priceElements = document.querySelectorAll('tr > td:nth-child(2):not(#sum)')
//     const sumElement = document.querySelector('#sum')
    
//     let sum = 0
//     priceElements.forEach(element => sum += Number(element.textContent))
//     sumElement.textContent = sum    
// }


function sumTable() {
    const priceElements = document.querySelectorAll('tr > td:nth-child(2):not(#sum)')
    const sumElement = document.querySelector('#sum')

    let sum = Array.from(priceElements).reduce((sum, price) => sum += Number(price.textContent), 0)    
    sumElement.textContent = sum
}

