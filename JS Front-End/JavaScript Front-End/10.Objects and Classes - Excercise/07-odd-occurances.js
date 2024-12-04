// function oddOccurances(input) {
//     let words = input.split(' ')
//     let wordOcurrances = {}
//     let result = ''

//     for (let word of words) {
//         word = word.toLowerCase()
//         if (!(wordOcurrances[word])) {
//             wordOcurrances[word] = 0
//         }
//         wordOcurrances[word]++;
//     }

//     wordOcurrances = Object.entries(wordOcurrances).filter(words => words[1] % 2 !== 0);    
//     for (let word of wordOcurrances) {
//         result += ` ${word[0]}`
//     }
//     console.log(result.trim());
// }

// oddOccurances('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')
// oddOccurances('Cake IS SWEET is Soft CAKE sweet Food')

function fancySolve(input) {
    let result = []
    let words = input.toLowerCase().split(' ')
    let inStock = words
        .reduce((result, word) => {
            return result.hasOwnProperty(word)
                ? {...result, [word]: result[word] + 1}
                : {...result, [word]: 1}
            } ,{});
    
    inStock = Object.entries(inStock)
        .filter(([element, count]) => count % 2 !== 0)
        .map(([element, count]) => element)
    console.log(inStock.join(' ')); 
}

fancySolve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')
fancySolve('Cake IS SWEET is Soft CAKE sweet Food')