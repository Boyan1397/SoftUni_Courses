function getWord(text) {
    let textArr = text.split(' ')
    let foundWords = textArr.filter(word => word.includes('#') && word.test(/^[a-zA-Z]+$/))
    foundWords.forEach(foundWord => {
        let result = foundWord.replace('#', '')
        console.log(result);
        
    });
}

getWord('Nowadays everyone uses # to tag a #special word in #socialMedia')
getWord('The symbol # is known #variously in English-speaking #regions as the #number sign')