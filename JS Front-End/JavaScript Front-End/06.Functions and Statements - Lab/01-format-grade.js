function returnGrade(grade) {

    let result = recieveGrade(grade)
    return result

    function recieveGrade(grade) {
        let status = ''
        if (grade >= 5.50) {
            status = 'Excellent'
        } else if (grade < 5.50 && grade >= 4.50) {
            status = 'Very good'
        } else if (grade < 4.50 && grade >= 3.50) {
            status = 'Good'
        } else if (grade < 3.50 && grade >= 3) {
            status = 'Poor'
        } else {
            status = 'Fail'
            return (`${status} (2)`);
        }

        return (`${status} (${grade.toFixed(2)})`);
    }

}

console.log(returnGrade(3.33));
console.log(returnGrade(4.50));
console.log(returnGrade(2.99));


