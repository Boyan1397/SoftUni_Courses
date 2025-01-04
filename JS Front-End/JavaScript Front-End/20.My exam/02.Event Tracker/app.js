window.addEventListener("load", solve);

function solve(){
    let saveButton = document.getElementById('save')
    let upcomingElement = document.getElementById('upcoming-list')
    let eventInput = document.getElementById('event')
    let noteInput = document.getElementById('note')
    let dateInput = document.getElementById('date')
    let eventsList = document.getElementById('events-list')
    let deleteButton = document.querySelector('.delete')
    let allEvents = document.getElementById('events')

    saveButton.addEventListener('click', () => {
        let event = eventInput.value
        let note = noteInput.value
        let date = dateInput.value
        // wraps
        let newEventLi = document.createElement('li')
        newEventLi.classList.add('event-item')
        let newEventContainerDiv = document.createElement('div')
        newEventContainerDiv.classList.add('event-container')
        // article and p
        let newArticle = document.createElement('article')
        let newEventP = document.createElement('p')
        newEventP.textContent = `Name: ${event}`
        let newNoteP = document.createElement('p')
        newNoteP.textContent = `Note: ${note}`
        let newDateP = document.createElement('p')
        newDateP.textContent = `Date: ${date}`
        // buttons
        let newButtonsDiv = document.createElement('div')
        newButtonsDiv.classList.add('buttons')
        let newEditButton = document.createElement('button')
        newEditButton.className = 'btn edit'
        newEditButton.textContent = 'Edit'
        let newDoneButton = document.createElement('button')
        newDoneButton.className = 'btn done'
        newDoneButton.textContent = 'Done'
        // appendchildren

        newArticle.appendChild(newEventP)
        newArticle.appendChild(newNoteP)
        newArticle.appendChild(newDateP)

        newButtonsDiv.appendChild(newEditButton)
        newButtonsDiv.appendChild(newDoneButton)

        newEventContainerDiv.appendChild(newArticle)
        newEventContainerDiv.appendChild(newButtonsDiv)
        
        newEventLi.appendChild(newEventContainerDiv)
        upcomingElement.appendChild(newEventLi)

        eventInput.value = ''
        noteInput.value = ''
        dateInput.value = ''

        newEditButton.addEventListener('click', () => {
            eventInput.value = event
            noteInput.value = note 
            dateInput.value = date

            newEventLi.remove()
        })

        newDoneButton.addEventListener('click', () => {
            eventsList.appendChild(newEventLi)
            newButtonsDiv.remove()
        })

        deleteButton.addEventListener('click', () => {
            if (deleteButton.parentElement === allEvents) {
                eventsList.remove()
            }
            
        })
    })
    
}
