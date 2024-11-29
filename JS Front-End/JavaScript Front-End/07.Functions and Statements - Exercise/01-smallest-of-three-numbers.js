// function getSmallest(a, b, c) {
//     smallest = Math.min(a, b, c)
//     console.log(smallest);   
// }

// getSmallest(2 , 4 ,235)


function getMinNumber(numbers) {
    let minNum = Number.MAX_SAFE_INTEGER
    for (let num of numbers) {
        if (num < minNum) {
            minNum = num
        }
    }
    return minNum
}

function solve(...numbers) {
    let result = getMinNumber(numbers)
    return result;
}   


console.log(solve(2, 4 ,235));
