function solve(first, second) {
    let numbers = '';
    let sumNumbers = 0;

    for (let i = first; i <= second; i++) {
        numbers += i + ' ';
        sumNumbers += i;
    }

    console.log(numbers.trim());
    console.log(`Sum: ${sumNumbers}`);

}

solve(5, 10)