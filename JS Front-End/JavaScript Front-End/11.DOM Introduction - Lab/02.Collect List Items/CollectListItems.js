function extractText() {
    let listItemsToAdd = document.getElementById('items');
    let textarea = document.getElementById('result');
    console.log(listItemsToAdd);
    

    textarea.textContent = listItemsToAdd.textContent
        .split('\n')
        .map(items => items.trim())
        .join('\n')
        .trim()

}

