function attachEvents() {
    let sendButton = document.getElementById('submit')
    let refreshButton = document.getElementById('refresh')
    let nameInputElement = document.querySelector('input[name="author"]')
    let messageInputElement = document.querySelector('input[name="content"]')    
    let textareaElement = document.getElementById('messages')
    textareaElement.textContent = ''

    sendButton.addEventListener('click', sendMessage)
    refreshButton.addEventListener('click', displayMessage)

    let myUrl = 'http://localhost:3030/jsonstore/messenger'
    async function sendMessage() {
        let nameInput = nameInputElement.value
        let messageInput = messageInputElement.value
        let body = {'author': nameInput, 'content': messageInput}
        let jsonBody = JSON.stringify(body)
        const response = await fetch(myUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonBody
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
    }

    async function displayMessage() {
        let response = await fetch(myUrl)
        let data = await response.json()
        let result = Object.values(data).map(messageInfo => `${messageInfo.author}: ${messageInfo.content}`)
        textareaElement.textContent = result.join('\n')

        nameInputElement.value = ''
        messageInputElement.value = ''

    }
}

attachEvents();