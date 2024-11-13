function solve(myNumbers) {

    let first = myNumbers.shift()
    let last = myNumbers.pop()
    console.log(first + last);
    
}

solve([20, 30, 40])