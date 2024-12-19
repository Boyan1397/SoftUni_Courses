window.addEventListener("load", solve);

function solve() {
    // get elements
    let addButton = document.getElementById('add-btn')
    let inputNameElement = document.getElementById('name')
    let inputPhoneElement = document.getElementById('phone')
    let inputCategoryElement = document.getElementById('category')
    let ulElement = document.getElementById('check-list')
    let ulContactElement = document.getElementById('contact-list')

    addButton.addEventListener('click', addAllElements)

    function addAllElements() {
        if (inputNameElement.value === '' || inputPhoneElement.value === '' || inputCategoryElement.value === '') return;
        // get input value
        let nameValue = inputNameElement.value
        let phoneValue = inputPhoneElement.value
        let categoryValue = inputCategoryElement.value
          // li and article
        let newLiElement = document.createElement('li')
        let newArticleElement = document.createElement('article')
        // p
        let newPNameElement = document.createElement('p')
        newPNameElement.textContent = `name:${nameValue}`
        let newPPhoneElement = document.createElement('p')
        newPPhoneElement.textContent = `phone:${phoneValue}`
        let newPCategory = document.createElement('p')
        newPCategory.textContent = `category:${categoryValue}`
        // buttons
        let newdivClassButton = document.createElement('div')
        newdivClassButton.classList.add('buttons')
        let newEditBtn = document.createElement('button')
        newEditBtn.classList.add('edit-btn')
        let newSaveBtn = document.createElement('button')
        newSaveBtn.classList.add('save-btn')

        newdivClassButton.appendChild(newEditBtn)
        newdivClassButton.appendChild(newSaveBtn)
        // appendchild
        newArticleElement.appendChild(newPNameElement)
        newArticleElement.appendChild(newPPhoneElement)
        newArticleElement.appendChild(newPCategory)

        newLiElement.appendChild(newArticleElement)
        newLiElement.appendChild(newdivClassButton)

        ulElement.appendChild(newLiElement)

        // clear input fields
        inputNameElement.value = ''
        inputPhoneElement.value = ''
        inputCategoryElement.value = '' 

        // edit buttton event listener

        newEditBtn.addEventListener('click', () => {
            inputNameElement.value = nameValue;
            inputPhoneElement.value = phoneValue;
            inputCategoryElement.value = categoryValue;  
            newLiElement.remove()
        })

        newSaveBtn.addEventListener('click', () => {
            ulContactElement.appendChild(newLiElement)
            newdivClassButton.remove()
            let deleteButton = document.createElement('button')
            deleteButton.classList.add('del-btn')
            newLiElement.appendChild(deleteButton)

            deleteButton.addEventListener('click', () => {
                newLiElement.remove()
            })
        })
    }
} 


//   // li and article
//   let newLiElement = document.createElement('li')
//   let newArticleElement = document.createElement('article')
//   // p
//   let newPNameElement = document.createElement('p')
//   newPNameElement.textContent = `name:${inputNameElement.value}`
//   let newPPhoneElement = document.createElement('p')
//   newPPhoneElement.textContent = `phone:${inputPhoneElement.value}`
//   let newPCategory = document.createElement('p')
//   newPCategory.textContent = `category:${inputCategoryElement.value}`
//   // buttons
//   let newdivClassButton = document.createElement('div')
//   newdivClassButton.classList.add('buttons')
//   let newEditBtn = document.createElement('button')
//   newEditBtn.classList.add('edit-btn')
//   let newSaveBtn = document.createElement('button')
//   newSaveBtn.classList.add('save-btn')

//   newdivClassButton.appendChild(newEditBtn)
//   newdivClassButton.appendChild(newSaveBtn)
//   // appendchild
//   newArticleElement.appendChild(newPNameElement)
//   newArticleElement.appendChild(newPPhoneElement)
//   newArticleElement.appendChild(newPCategory)

//   newLiElement.appendChild(newArticleElement)
//   newLiElement.appendChild(newdivClassButton)

//   ulElement.appendChild(newLiElement)

//   // clear input fields
//   inputNameElement.value = ''
//   inputPhoneElement.value = ''
//   inputCategoryElement.value = '' 

//   // edit buttton event listener

//   newEditBtn.addEventListener('click', () => {