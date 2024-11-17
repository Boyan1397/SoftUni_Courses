// function findString(word, text) {
//     let textArr = text.split(' ')
//     textArr = textArr.map(wrd => wrd.toLowerCase())
//     let resultArr = textArr.filter(wrd => wrd === word)
    
//     if (resultArr.length > 0) {
//         console.log(word);
//     } else {
//         console.log(`${word} not found!`);
        
//     }
// }

// findString('javascript', 'JavaScript is the best programming language')
// findString('python', 'JavaScript is the best programming language')



function findStrings(word, text) {
    text = text.toLowerCase().split(' ')
    if (text.includes(word)) {
        console.log(word);
        
    } else {
        console.log(`${word} not found!`);
    }  
}


findStrings('javascript', 'JavaScript is the best programming language')
findStrings('python', 'JavaScript is the best programming language')