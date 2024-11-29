function getCharsBetween(first, second) {
        let arrayOfCharacters = []

        let chars = [first, second]
        chars.sort()

        let start = chars[0].charCodeAt(0)
        let end = chars[1].charCodeAt(0)
    
        for (i = start + 1; i < end; i++) {
            arrayOfCharacters.push(String.fromCharCode(i))
        }
        console.log(...arrayOfCharacters); 
    }

getCharsBetween('a', 'd');
getCharsBetween('#', ':');
getCharsBetween('C', '#');

// function solve(first, second) {
//     let [start, end] = sortChars(first, second)
//     let numsBetween = getNumbersBetween(start, end)
//     let result = numsBetween.map(num => String.fromCharCode(num))
//     return result.join(' ')

//     function sortChars(first, second) {
//         let chars = [first, second]
//         chars.sort()
//         return chars
//     }
    
//     function getNumbersBetween(first, second) {
//         let num1 = first.charCodeAt(0)
//         let num2 = second.charCodeAt(0)
//         let nums = []
    
//         for (let i = num1 + 1; i < num2; i ++) {
//             nums.push(i)
//         }
//         return nums
//     }
// }

// console.log(solve('a', 'd'));
// console.log(solve('#', ':'));
// console.log(solve('C', '#'));

