// function reveal(searchedWords, text) {
//     let textArr = text.split(' ');
//     let searchedArr = searchedWords.split(', ');    let textResult = ''
    
//     textArr.forEach(word => {
//         if (word.includes('*')) {
//             searchedArr.forEach (searched => {
//                 if (word.length === searched.length) {
//                     let textResult = textArr.join(' ');
//                     textResult = textResult.replace(word, searched)
//                     textArr = textResult.split(' ')
                                        
//                 }

                
//             }
//             )           
//         }
    
   
//     });
//     console.log(textArr.join(' '));
    
// }

// reveal('great', 'softuni is ***** place for learning new programming languages')
// reveal('great, learning', 'softuni is ***** place for ******** new programming languages')


function reveals(wordsInput, textInput) {
    let wordsArr = wordsInput.split(', ')
    let textArr = textInput.split(' ')

    textArr = textArr.map(word => word[0] === '*' 
        ? wordsArr.find(w => w.length === word.length)
        : word)
    console.log(textArr.join(' '));
    
}

reveals('great', 'softuni is ***** place for learning new programming languages')
reveals('great, learning', 'softuni is ***** place for ******** new programming languages')
