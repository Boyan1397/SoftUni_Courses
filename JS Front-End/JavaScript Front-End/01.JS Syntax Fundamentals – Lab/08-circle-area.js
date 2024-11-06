function calculateArea(value) {
    if (typeof(value) === 'number') {
        let area = (Math.PI * Math.pow(value, 2)).toFixed(2)
        console.log(area)
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(value)}.`)
    }
}

calculateArea(5)
calculateArea('asdads')