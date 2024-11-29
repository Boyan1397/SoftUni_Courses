function solve(actions) {
    let cleanPercent = 0

    actions.forEach(action => {
        if (action === 'soap') {
            cleanPercent += 10
        } else if (action === 'water') {
            cleanPercent += cleanPercent * 0.2
        } else if (action === 'vacuum cleaner') {
            cleanPercent += cleanPercent * 0.25
        } else {
            cleanPercent *= 0.90
        }        
    });

    console.log(`The car is ${cleanPercent.toFixed(2)}% clean.`);
}

solve(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water'])