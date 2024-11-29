function solve(a, b) {
    let first = calculateFactorial(a);
    let second = calculateFactorial(b);
    return (first / second).toFixed(2)

    function calculateFactorial(number) {
        if (number === 1) {
            return 1
        }
    
        let result = number * calculateFactorial(number - 1)
        return result
    }
    
}

console.log(solve(5, 2));
