function solve(myString) {
    let wordsString = myString.match(/\w+/g);
    console.log(wordsString);
    
    wordsString = wordsString.join(', ')
    console.log(wordsString.toUpperCase());
    
    
}

solve('Hi, how are you?')