// function censorWords(sentence, word) {
//     let wordLength = word.length
//     let result = sentence.replaceAll(word, '*'.repeat(wordLength))
//     return result
// }
// console.log(censorWords('A small sentence with some words', 'small'));

function censorsWords(sentence, word) {
    let index = sentence.indexOf(word)

    while (index >= 0) {
        sentence = sentence.replace(word, '*'.repeat(word.length))
        index = sentence.indexOf(word)
    }
    return sentence
}

console.log(censorsWords('A small sentence with some small words', 'small'));

