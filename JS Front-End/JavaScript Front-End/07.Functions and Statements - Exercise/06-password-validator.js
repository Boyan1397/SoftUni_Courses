function solve(password) {
    const isLengthValid = password => password.length >= 6 && password.length <= 10;
    const isOnlyLettersAndDigits = password => /^[A-Za-z0-9]+$/.test(password)
    const isStrong = password => password
        .split('')
        .filter(char => !isNaN(char))
        .length >= 2;

    let isValid = true
    
    if (!isLengthValid(password)) {
        console.log("Password must be between 6 and 10 characters");   
        isValid = false
    }

    if (!isOnlyLettersAndDigits(password)) {
        console.log("Password must consist only of letters and digits");  
        isValid = false
    }
    
    if (!isStrong(password)) {
        console.log("Password must have at least 2 digits");
        isValid = false
    }

    if (isValid) {
        console.log('Password is valid');
    }
}

solve('logIn')
solve('MyPass123')
solve('Pa$s$s')