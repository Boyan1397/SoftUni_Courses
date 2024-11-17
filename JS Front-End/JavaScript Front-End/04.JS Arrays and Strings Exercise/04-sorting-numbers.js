function sortArr(numbers) {
    let result = []
    numbers.sort((a, b) => a - b)

    while (numbers.length > 0) {
        let firstNumber = numbers.shift()
        let lastNumber = numbers.pop()

        result.push(firstNumber, lastNumber)
    }
    return result 
}

console.log(sortArr([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));

