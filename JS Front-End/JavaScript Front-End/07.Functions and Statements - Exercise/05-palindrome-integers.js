function solve(numbers) {
    numbers.forEach(printPalindromeResult)
}

function isPlaindrome(numbers) {
    let normalNum = numbers.toString()
    let reversedNum = numbers.toString().split('').reverse().join('')
    return normalNum === reversedNum
    
}

function printPalindromeResult(numbers) {
    console.log(isPlaindrome(numbers));
    
}

solve([123,323,421,121])