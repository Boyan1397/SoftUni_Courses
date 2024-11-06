
function solve(a, b, sign) {

    let result;
    switch(sign) {
        case '+':
            result = (a + b);
            break;
        case '-':
            result = (a - b);
            break;
        case '*':
            result = (a * b);
            break;
        case '/':
            result = (a / b);
            break;
        case '%':
            result = (a % b);
            break;
        case '**':
            result = (a ** b);
            break;    
    }

    console.log(result);
}

solve(2, 4, '-')