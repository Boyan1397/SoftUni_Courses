// function deleteByEmail() {
//     let emailsElements = document.querySelectorAll('tbody tr td:nth-child(2)')
//     let inputElement = document.querySelector('input')
//     let resultElement = document.querySelector('#result')

//     let input = inputElement.value

//     for (let emailElement of emailsElements) {
//         if (emailElement.textContent === input) {
//             emailElement.parentElement.remove()
//             resultElement.textContent = 'Deleted.'
//         } else {
//             resultElement.textContent = 'Not found.'
//         }
//     }

//     inputElement.value = ''
    
//     console.log('TODO:...');
// }


function deleteByEmail() {
    let rowElements = document.querySelectorAll('tbody tr')
    let inputElement = document.querySelector('input')
    let resultElement = document.querySelector('#result')

    let input = inputElement.value

    for (let rowElement of rowElements) {
        if (rowElement.textContent.includes(input)) {
            rowElement.remove()
            resultElement.textContent = 'Deleted'
        } else {
            resultElement.textContent = 'Not found.'
        }
    }

    inputElement.value = ''
    console.log('TODO:...');
}