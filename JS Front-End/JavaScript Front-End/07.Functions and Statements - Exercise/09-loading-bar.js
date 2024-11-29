function solve(number) {
    number = number / 10
    let loadingBar = createLoadingBar(number)
    
    if (number < 10) {
        console.log(`${number * 10}% [${loadingBar.join('')}]`);
        console.log('Still loading...');
    } else {
        console.log('100% Complete!');
        console.log(`[${loadingBar.join('')}]`);
    }

    function createLoadingBar(number) {
        let loadingBar = Array(10).fill('.')
        loadingBar.fill('%', 0, number)
        return loadingBar
    }
}

solve(30)
solve(50)
solve(100)