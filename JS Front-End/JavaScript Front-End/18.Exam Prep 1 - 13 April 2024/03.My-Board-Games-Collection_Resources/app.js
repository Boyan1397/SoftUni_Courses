// let loadGamesButtonElement = document.getElementById('load-games')
// let gamesListElement = document.getElementById('games-list')

// let addGameButton = document.getElementById('add-game')
// let editGameButton = document.getElementById('edit-game')
// let inputNameElement = document.getElementById('g-name')
// let inputTypeElement = document.getElementById('type')
// let inputPlayersElement = document.getElementById('players')


// baseUrl = 'http://localhost:3030/jsonstore/games'

// loadGamesButtonElement.addEventListener('click', loadGame)

// // TODO
// function loadGame() {
//     fetch(baseUrl)
//         .then(response => response.json())
//         .then(data => {
//             gamesListElement.innerHTML = ''
//             let games = Object.values(data)
//             for (let game of games) {
//                 addGame(game)
//             }
//         })

// }


// addGameButton.addEventListener('click', () => {
// addGameButton.disabled = false
// let inputName = inputNameElement.value
// let inputType = inputTypeElement.value
// let inputPlayers = inputPlayersElement.value
// let objBody = {name: inputName, type: inputType, players: inputPlayers}

// fetch(baseUrl, {
//     method: 'POST',
//     headers: {
//             'Content-Type': 'application/json'
//             },
//     body: JSON.stringify(objBody)
//     })
//     .then(response => response.json())
//     .then(data => {
//         addGame(data)
//     })
//     inputNameElement.value = ''
//     inputTypeElement.value = ''
//     inputPlayersElement.value = '' 

// })

// function addGame(game) {
//     let newWrapperDiv = document.createElement('div')
//     newWrapperDiv.classList.add('board-game')
//     let newContentDiv = document.createElement('div')
//     newContentDiv.classList.add('content')
//     // create p
//     let newNameP = document.createElement('p')
//     newNameP.textContent = game.name
//     let newPlayersP = document.createElement('p')
//     newPlayersP.textContent = game.players
//     let newTypeP = document.createElement('p')
//     newTypeP.textContent = game.type
//     // create buttons
//     let newButtonsDiv = document.createElement('div')
//     newButtonsDiv.classList.add('buttons-container')
//     let newChangeButton = document.createElement('button')
//     newChangeButton.classList.add('change-btn')
//     newChangeButton.textContent = 'Change'
//     let newDeleteButton = document.createElement('button')
//     newDeleteButton.classList.add('delete-btn')
//     newDeleteButton.textContent = 'Delete'
    
//     newDeleteButton.addEventListener('click', () => {
//         console.log(game._id);
        
//         fetch(baseUrl + `/${game._id}`, {
//             method: 'DELETE'
//         }) 
//     })

//     // appendchild
//     newContentDiv.appendChild(newNameP)
//     newContentDiv.appendChild(newTypeP)
//     newContentDiv.appendChild(newPlayersP)

//     newButtonsDiv.appendChild(newChangeButton)
//     newButtonsDiv.appendChild(newDeleteButton)

//     newWrapperDiv.appendChild(newContentDiv)
//     newWrapperDiv.appendChild(newButtonsDiv)
//     gamesListElement.appendChild(newWrapperDiv)

//     newChangeButton.addEventListener('click', () => {
//         addGameButton.disabled = true
//         editGameButton.disabled = false
//         inputNameElement.value = newNameP.textContent
//         inputTypeElement.value = newTypeP.textContent
//         inputPlayersElement.value = newPlayersP.textContent

//         editGameButton.addEventListener('click', () => {
//             let inputName = inputNameElement.value
//             let inputType = inputTypeElement.value
//             let inputPlayers = inputPlayersElement.value
//             let objBody = {name: inputName, type: inputType, players: inputPlayers}     
//             console.log(game);
//             fetch(baseUrl + `/${game._id}`, {
//                 method: 'PUT',
//                 headers: {
//                     "Content-Type": "application/json", 
//                 },
//                 body: JSON.stringify(objBody)
//             })
//             editGameButton.disabled = true
//             addGameButton.disabled = false
//         })
//     })
    
// }



let loadGamesButtonElement = document.getElementById('load-games');
let gamesListElement = document.getElementById('games-list');
let addGameButton = document.getElementById('add-game');
let editGameButton = document.getElementById('edit-game');
let inputNameElement = document.getElementById('g-name');
let inputTypeElement = document.getElementById('type');
let inputPlayersElement = document.getElementById('players');
let currentGameId = null;

const baseUrl = 'http://localhost:3030/jsonstore/games';

// Load Games Function
loadGamesButtonElement.addEventListener('click', loadGames);

async function loadGames() {
    try {
        const response = await fetch(baseUrl);
        const data = await response.json();
        gamesListElement.innerHTML = '';
        let games = Object.values(data);
        games.forEach(game => addGame(game));
    } catch (error) {
        console.error('Error loading games:', error);
    }
}

// Add Game Function
addGameButton.addEventListener('click', async () => {
    addGameButton.disabled = false;
    let inputName = inputNameElement.value;
    let inputType = inputTypeElement.value;
    let inputPlayers = inputPlayersElement.value;
    let objBody = { name: inputName, type: inputType, players: inputPlayers };

    try {
        const response = await fetch(baseUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(objBody),
        });
        const newGame = await response.json();
        addGame(newGame);
    } catch (error) {
        console.error('Error adding game:', error);
    }

    inputNameElement.value = '';
    inputTypeElement.value = '';
    inputPlayersElement.value = '';
});

// Add Game to UI
function addGame(game) {
    let newWrapperDiv = document.createElement('div');
    newWrapperDiv.classList.add('board-game');
    let newContentDiv = document.createElement('div');
    newContentDiv.classList.add('content');

    let newNameP = document.createElement('p');
    newNameP.textContent = game.name;
    let newPlayersP = document.createElement('p');
    newPlayersP.textContent = game.players;
    let newTypeP = document.createElement('p');
    newTypeP.textContent = game.type;

    let newButtonsDiv = document.createElement('div');
    newButtonsDiv.classList.add('buttons-container');

    let newChangeButton = document.createElement('button');
    newChangeButton.classList.add('change-btn');
    newChangeButton.textContent = 'Change';

    let newDeleteButton = document.createElement('button');
    newDeleteButton.classList.add('delete-btn');
    newDeleteButton.textContent = 'Delete';

    newContentDiv.appendChild(newNameP);
    newContentDiv.appendChild(newTypeP);
    newContentDiv.appendChild(newPlayersP);

    newButtonsDiv.appendChild(newChangeButton);
    newButtonsDiv.appendChild(newDeleteButton);

    newWrapperDiv.appendChild(newContentDiv);
    newWrapperDiv.appendChild(newButtonsDiv);
    gamesListElement.appendChild(newWrapperDiv);

    newChangeButton.addEventListener('click', () => loadGameToForm(game));
    newDeleteButton.addEventListener('click', () => deleteGame(game._id));
}

// Load Game to Form for Editing
function loadGameToForm(game) {
    addGameButton.disabled = true;
    editGameButton.disabled = false;
    currentGameId = game._id;

    inputNameElement.value = game.name;
    inputTypeElement.value = game.type;
    inputPlayersElement.value = game.players;

    editGameButton.addEventListener('click', () => editGame(game));
}

// Edit Game Function
async function editGame(game) {
    let inputName = inputNameElement.value;
    let inputType = inputTypeElement.value;
    let inputPlayers = inputPlayersElement.value;
    let objBody = { name: inputName, type: inputType, players: inputPlayers };

    try {
        const response = await fetch(`${baseUrl}/${game._id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(objBody),
        });
        const updatedGame = await response.json();
        addGame(updatedGame);
    } catch (error) {
        console.error('Error editing game:', error);
    }

    // Reset UI
    editGameButton.disabled = true;
    addGameButton.disabled = false;
    inputNameElement.value = '';
    inputTypeElement.value = '';
    inputPlayersElement.value = '';
}

// Delete Game Function
async function deleteGame(gameId) {
    try {
        await fetch(`${baseUrl}/${gameId}`, {
            method: 'DELETE',
        });

        // Reload games after successful deletion
        loadGames();
    } catch (error) {
        console.error('Error deleting game:', error);
    }
}
