// arrow statement body USED FOR IFS AND LOOPS AND ETC.
let checkAndSum = (a, b) => {
    if (a > b) {
        console.log('A is bigger');
        return(a, b) => a * b
    }
}

console.log(checkAndSum(123, 5));


// arrow expression body USED FOR SINGLE USE AND RETURN
let sum = (a, b) => a + b;
console.log(sum(15, 20));
