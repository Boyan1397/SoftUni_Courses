document.addEventListener('DOMContentLoaded', solve);

function solve() {
    let formEncodeElement = document.getElementById('encode')
    let formDecodeElement = document.getElementById('decode')

    formEncodeElement.addEventListener('submit', (e) => {
        e.preventDefault()
        let inputElement = formEncodeElement.querySelector('textarea')
        let codedMessage = inputElement.value.split('').map(char => String.fromCharCode(char.charCodeAt(0) + 1)) .join('')       
        
        formDecodeElement.querySelector('textarea').value = codedMessage
        inputElement.value = ''
    })

    formDecodeElement.addEventListener('submit', (e) => {
        e.preventDefault()
        let inputElement = formDecodeElement.querySelector('textarea')
        let decodedMessage = inputElement.value.split('').map(char => String.fromCharCode(char.charCodeAt(0) - 1)).join('')

        inputElement.value = decodedMessage
    })
}