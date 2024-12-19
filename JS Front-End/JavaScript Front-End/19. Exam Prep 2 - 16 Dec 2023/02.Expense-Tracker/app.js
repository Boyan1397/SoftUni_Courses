window.addEventListener("load", solve);

function solve() {
    let expenseInputElement = document.getElementById('expense')
    let amountInputElement = document.getElementById('amount')
    let dateInputElement = document.getElementById('date')
    let addButtonElement = document.getElementById('add-btn')
    let previewListElement = document.getElementById('preview-list')
    let expensesListElement = document.getElementById('expenses-list')

    // ADD BUTTON LISTENER
    addButtonElement.addEventListener('click', () => {
        let type = expenseInputElement.value
        let amount = amountInputElement.value
        let date = dateInputElement.value
        
        if ((!type || !amount || !date)) return;
        
        let newLiExpenseItemElement = document.createElement('li')
        newLiExpenseItemElement.classList.add('expense-item')

        // article and p
        let newArticleElement = document.createElement('article')

        let newExpenseTypePElement = document.createElement('p')
        newExpenseTypePElement.textContent = `Type: ${type}`

        let newAmountPElement = document.createElement('p')
        newAmountPElement.textContent = `Amount: ${amount}$`

        let newDatePElement = document.createElement('p')
        newDatePElement.textContent = `Date: ${date}`

        // buttons
        let newButtonsDiv = document.createElement('div')
        newButtonsDiv.classList.add('buttons')

        let newEditButton = document.createElement('button')
        newEditButton.className = 'btn edit'
        newEditButton.textContent = 'edit'

        let newOkButton = document.createElement('button')
        newOkButton.className = 'btn ok'
        newOkButton.textContent = 'ok'

        // appendchildren
        newArticleElement.appendChild(newExpenseTypePElement)
        newArticleElement.appendChild(newAmountPElement)
        newArticleElement.appendChild(newDatePElement)

        newButtonsDiv.appendChild(newEditButton)
        newButtonsDiv.appendChild(newOkButton)

        newLiExpenseItemElement.appendChild(newArticleElement)
        newLiExpenseItemElement.appendChild(newButtonsDiv)

        previewListElement.appendChild(newLiExpenseItemElement)

        expenseInputElement.value = ''
        amountInputElement.value = ''
        dateInputElement.value = ''
        addButtonElement.disabled = true

        // EDIT BUTTON LISTENER
        newEditButton.addEventListener('click', () => {
            newLiExpenseItemElement.remove()
            expenseInputElement.value = type
            amountInputElement.value = amount
            dateInputElement.value = date
            addButtonElement.disabled = false
        })

        // OK BUTTON
        newOkButton.addEventListener('click', () => {
            expensesListElement.appendChild(newLiExpenseItemElement)
            newButtonsDiv.remove()
            addButtonElement.disabled = false
        })

        // DELETE BUTTON
        let newDeleteButton = document.createElement('button')
        newDeleteButton.className = 'btn delete'
        newDeleteButton.textContent = 'Delete'
        
        newDeleteButton.addEventListener('click', () => {
            newLiExpenseItemElement.remove()
        })
        
    })
}
