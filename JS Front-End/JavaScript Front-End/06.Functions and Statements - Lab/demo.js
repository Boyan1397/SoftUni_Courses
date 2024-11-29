let arrow = (text) => console.log(text);

let exp = function (text) {
    console.log(text + ' ' + text);
}


function masterFunc(name) {
    
    exp(`2 - ${name}`)
}

masterFunc('Bobo')


// recursion
function myRecursion(x) {
    console.log(x);
    if (x > 1) {
        myRecursion(x - 1)
    }
    
}

myRecursion(10)


function someNum() {
    console.log('its 2');
    return 'sfarqw'
    
}



function outerFunction(outerValue) {
    return function nestedFunction(innerValue) {
        console.log(`Outer value: ${outerValue}, Inner value: ${innerValue}`);
    };
}

const innerFunc = outerFunction("Outer");
innerFunc("Inner");


