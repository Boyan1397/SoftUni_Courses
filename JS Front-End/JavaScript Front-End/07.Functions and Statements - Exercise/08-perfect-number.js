function solve(number) {
    let devisors = getAllDevisors(number);
    let devisorsSum = sumDevisors(devisors);
    if (devisorsSum === number) {
        return "We have a perfect number!"
    }
    return "It's not so perfect."

    function getAllDevisors(number) {
        let devisors = []
    
        for (let i = 1; i < ((number / 2) + 1); i++) {
            if (number % i === 0) {
                devisors.push(i)
            }
        }
        return devisors
        
    }
    
    function sumDevisors(devisorsArr) {
        return devisorsArr.reduce((num, sum) => sum += num, 0)
    }
}

console.log(solve(6));
console.log(solve(28));
console.log(solve(1236498));
