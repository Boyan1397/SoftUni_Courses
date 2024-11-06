function solve(firstNumber, secondNumber, thirdNumber) {
    
    let largest;
    if (firstNumber > secondNumber && firstNumber > thirdNumber) {
        largest = firstNumber
    } else if (secondNumber > firstNumber && secondNumber > thirdNumber) {
        largest = secondNumber
    } else  {
        largest = thirdNumber
    }
    console.log(`The largest number is ${largest}.`);
}

solve(5, -3, 16)
solve(-3, -5, -22.5)


function hackySolve(a, b, c) {
    let result;
    result = Math.max(a, b, c)

    console.log(`The largest number is ${result}.`);
    
}

hackySolve(5, -3, 16)
hackySolve(-3, -5, -22.5)