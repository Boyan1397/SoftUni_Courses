function logins(dataArr) {
    let username = dataArr.shift()
    reversedUsername = username.split('').reverse().join('')
    let counter = 0

    for (i = 0; i < dataArr.length; i++) {
        counter += 1
        
        if (reversedUsername === dataArr[i]) {
            return `User ${username} logged in.`
        } else {
            if (counter >= 4) {
                return `User ${username} blocked!`
            }
            console.log('Incorrect password. Try again.');  
        }
    }
}

console.log(logins(['Acer','login','go','let me in','recA']));
console.log(logins(['momo','omom']));
console.log(logins(['sunny','rainy','cloudy','sunny','not sunny']));



// function login(dataArr) {
//     const username = dataArr.shift()
//     let wordsArr = [];
//     let counter = 0
    
//     for (word of dataArr) {
//         let currentWord = word.split('').reverse()
//         currentWord = currentWord.join('')
//         counter += 1
        
//         if (username === currentWord) {
//             return `User ${username} logged in.`
//         } else {
//             if (counter >= 4) {
//                 return `User ${username} blocked!`
//             }
//             console.log('Incorrect password. Try again.');
            
//         }
//     }
// }

// console.log(login(['Acer','login','go','let me in','recA']));
// console.log(login(['momo','omom']));
// console.log(login(['sunny','rainy','cloudy','sunny','not sunny']));




