function countStrings(text, word) {
    text = text
        .split(' ')
        .filter(wrd => wrd === word)
        .length
    
    return text
}

console.log(countStrings('This is a word and it also is a sentence', 'is'));


// function countString(text, word) {
//     let count = 0
//     let arrText = text.split(' ')
//     for (let wrd of arrText) {
//         if (word === wrd) {
//             count += 1
//         }
//     }
//     return count
// }

// console.log(countString('This is a word and it also is a sentence', 'is'));

