// function wordsTracker(wordsArray) {
//     let dataCounter = {}
//     let searcheWords = wordsArray.shift().split(' ');
    
//     for (let searched of searcheWords) {
//         dataCounter[searched] = 0
//         for (let word of wordsArray) {
//             if (searched === word) {
//                 dataCounter[searched] += 1
//             } 
//         }
//     }
    
//     dataCounter = Object.entries(dataCounter).sort((a, b) => b[1] - a[1])
//     dataCounter = Object.fromEntries(dataCounter)

//     for (let word in dataCounter) {
//         console.log(`${word} - ${dataCounter[word]}`);
//     }   
// }

function fancyTracker(wordsArray) {
    let searcheWords = wordsArray
        .shift()
        .split(' ')
        .reduce((result, word) => {
            result[word] = 0
            return result
        }, {});
    
    for (let word of wordsArray) {
        if (searcheWords.hasOwnProperty(word)) {
            searcheWords[word] += 1
        }
    }
    
    searcheWords = Object.entries(searcheWords).sort((a, b) => b[1] - a[1])
    searcheWords = Object.fromEntries(searcheWords)

    for(let word in searcheWords) {
        console.log(`${word} - ${searcheWords[word]}`);
    }
};

fancyTracker([  
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
]);

fancyTracker([
    'is the',
    'first', 'sentence', 'Here', 'is',
    'another', 'the', 'And', 'finally', 'the',
    'the', 'sentence'
])

// function wordsTracker(wordsArray) {
//     let dataCounter = {}
//     let searcheWords = wordsArray.shift().split(' ');
    
//     for (let searched of searcheWords) {
//         dataCounter[searched] = 0
//         for (let word of wordsArray) {
//             if (searched === word) {
//                 dataCounter[searched] += 1 
//                 }
//             } 

//         }
    
//     dataCounter = Object.entries(dataCounter).sort((a, b) => b[1] - a[1])
//     dataCounter = Object.fromEntries(dataCounter)
    
//     for (let word in dataCounter) {
//         console.log(`${word} - ${dataCounter[word]}`);
//     } 
//     }
    
      


// wordsTracker([  
//             'this sentence',
//             'In', 'this', 'sentence', 'you', 'have',
//             'to', 'count', 'the', 'occurrences', 'of',
//             'the', 'words', 'this', 'and', 'sentence',
//             'because', 'this', 'is', 'your', 'task'
//         ]);

// wordsTracker([
//             'is the',
//             'first', 'sentence', 'Here',
//             'another', 'the', 'And', 'finally', 'the',
//             'the', 'sentence'
//         ])
