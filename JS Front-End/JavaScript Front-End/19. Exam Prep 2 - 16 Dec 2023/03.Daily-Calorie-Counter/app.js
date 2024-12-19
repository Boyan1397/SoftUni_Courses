let loadMealsButton = document.getElementById('load-meals')
let addMealButton = document.getElementById('add-meal')
let editMealButton = document.getElementById('edit-meal')
let listHolder = document.getElementById('list')
let foodInputEl = document.getElementById('food')
let timeInputEl = document.getElementById('time')
let caloriesInputEl = document.getElementById('calories')

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
let currentMealId = null

loadMealsButton.addEventListener('click', loadMeals)
addMealButton.addEventListener('click', addMeal)
editMealButton.addEventListener('click', editMeal)

let baseUrl = 'http://localhost:3030/jsonstore/tasks'

async function loadMeals() {
    let response = await fetch(baseUrl)
    let data = await response.json()
    listHolder.innerHTML = ''
    for (let meal of Object.values(data)) {
        let food = meal.food
        let time = meal.time
        let calories = meal.calories

        let newMealDiv = document.createElement('load-meals')
        newMealDiv.classList.add('meal') 
        let newFoodH2 = document.createElement('h2')
        newFoodH2.textContent = food

        let newTimeH3 = document.createElement('h3')
        newTimeH3.textContent = time

        let newCaloriesH3 = document.createElement('h3')
        newCaloriesH3.textContent = calories
        // buttons
        let newMealButtonsDiv = document.createElement('div')
        newMealButtonsDiv.id = 'meal-buttons'
        let newChangeButton = document.createElement('button')
        newChangeButton.classList.add('change-meal')
        newChangeButton.textContent = 'Change'

        let newDeleteButton = document.createElement('button')
        newDeleteButton.classList.add('delete-meal')
        newDeleteButton.textContent = 'Delete'

        newMealButtonsDiv.appendChild(newChangeButton)
        newMealButtonsDiv.appendChild(newDeleteButton)

        newMealDiv.appendChild(newFoodH2)
        newMealDiv.appendChild(newTimeH3)
        newMealDiv.appendChild(newCaloriesH3)
        newMealDiv.appendChild(newMealButtonsDiv)

        listHolder.appendChild(newMealDiv)

        newChangeButton.addEventListener('click', () => {
            // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            currentMealId = meal._id
            newMealDiv.remove()
            foodInputEl.value = meal.food
            timeInputEl.value = meal.time
            caloriesInputEl.value = meal.calories
            editMealButton.disabled = false 
            addMealButton.disabled = true   
        })

        newDeleteButton.addEventListener('click', async () => {
            let response = await fetch(`${baseUrl}/${meal._id}`, {
                method: 'DELETE'
            })
            loadMeals()
            newMealDiv.remove()

        })
    }
    
}

async function addMeal() {
    let food = foodInputEl.value
    let time = timeInputEl.value
    let calories = caloriesInputEl.value
    let objBody = {food, calories, time}

    let response = await fetch(baseUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(objBody),
    })
// todo
    if (!response.ok) {
        return
    }

    foodInputEl.value = ''
    timeInputEl.value = ''
    caloriesInputEl.value = ''

    loadMeals()
}

async function editMeal() {
    let food = foodInputEl.value
    let time = timeInputEl.value
    let calories = caloriesInputEl.value
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    let objBody = {food, calories, time, _id: currentMealId}

    let response = await fetch(`${baseUrl}/${currentMealId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(objBody)
    })

    if (!response.ok) {
        return
    }

    foodInputEl.value = ''
    timeInputEl.value = ''
    caloriesInputEl.value = ''
    // !!!!!!!!!!!!!!
    currentMealId = null

    editMealButton.disabled = true
    addMealButton.disabled = false
    loadMeals()
}



