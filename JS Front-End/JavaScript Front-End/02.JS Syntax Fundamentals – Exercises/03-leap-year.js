function solve(year) {
    let leap;
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
        leap = 'yes'
    } else {
        leap = 'no'
    }

    console.log(leap);   
}

solve(2003)
solve(1984)
solve(4)