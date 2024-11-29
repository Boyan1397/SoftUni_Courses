function solve(number) {
    let numberArr = number
        .toString()
        .split('')
        .map(Number);
    
    let average = getAverage(numberArr)
    
    while (average <= 5 ) {
        numberArr.push(9)
        average = getAverage(numberArr);
    }

    return numberArr.join('')
    
}

function getAverage(numberArr) {
        let sum = numberArr.reduce((num, sum) => sum += num, 0)
        return sum / numberArr.length
}

console.log(solve(101));
console.log(solve(5835));