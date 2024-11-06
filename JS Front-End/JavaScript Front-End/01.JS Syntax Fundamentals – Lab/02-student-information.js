// `Name: {student name}, Age: {student age}, Grade: {student grade}`


function solve(name, age, grade) {
    let info = (`Name: ${name}, Age: ${age}, Grade: ${grade.toFixed(2)}`)
    console.log(info);
}

solve('John', 15, 5.54678)
solve('Steve', 16, 2.1426)
solve('Marry', 12, 6.00)
