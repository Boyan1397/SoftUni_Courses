function solve(input) {
    let count = input.shift()
    let team = {}
    for (let i = 0; i < count; i++) {
        let [name, shift, ...coffees] = input.shift().split(' ')
        coffees = coffees.join(',').split(',')
        team[name] = {shift, coffees}
    }
    
    let commandLine = input.shift()
    while (commandLine !== 'Closed') {
        let [command, workerName, ...args] = commandLine.split(' / ')
        switch(command) {
            case 'Prepare':
                let [shift, coffee] = args
                if (team[workerName].coffees.includes(coffee) && team[workerName].shift === shift) {
                    console.log(`${workerName} has prepared a ${coffee} for you!`);
                } else {
                    console.log(`${workerName} is not available to prepare a ${coffee}.`);
                }
                break;
        
            case 'Change Shift':
                let newShift = args[0]
                team[workerName].shift = newShift
                console.log(`${workerName} has updated his shift to: ${newShift}`);
                break;
            
            case 'Learn':
                let newCoffee = args[0]
                if (team[workerName].coffees.includes(newCoffee)) {
                    console.log(`${workerName} knows how to make ${newCoffee}.`);
                } else {
                    team[workerName].coffees.push(newCoffee)
                    console.log(`${workerName} has learned a new coffee type: ${newCoffee}.`);
                    
                }
                break;
        }
        commandLine = input.shift()
    }

    for (let name in team) {
        let coffees = team[name].coffees.join(', ');
        console.log(`Barista: ${name}, Shift: ${team[name].shift}, Drinks: ${coffees}`);
    }
}
// {shift: 'day', coffees: Array(1)}
// {shift: 'night', coffees: Array(1)}
// {shift: 'day', coffees: Array(1)}
solve([

    '3',
    
    'Alice day Espresso,Cappuccino',
    
    'Bob night Latte,Mocha',
    
    'Carol day Americano,Mocha',
    
    'Prepare / Alice / day / Espresso',
    
    'Change Shift / Bob / night',
    
    'Learn / Carol / Latte',
    
    'Learn / Bob / Latte',
    
    'Prepare / Bob / night / Latte',
    
    'Closed'
])
