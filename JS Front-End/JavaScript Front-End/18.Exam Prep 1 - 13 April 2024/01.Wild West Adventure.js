function solve(inputPosses) {
    let charsCount = inputPosses.shift()
    let characters = {}

    for (let i = 0; i < charsCount; i++) {
        let [name, health, bullets] = inputPosses.shift().split(' ')
        health = Number(health)
        bullets = Number(bullets)
        characters[name] = {hp: health, bullets: bullets}
    }
    
    let commandLine = inputPosses.shift()
    while (commandLine !== "Ride Off Into Sunset") {
        let [command, name, ...args] = commandLine.split(' - ');

        if (command === 'FireShot') {
            if (characters[name].bullets) {
                characters[name].bullets -= 1
                console.log(`${name} has successfully hit ${args[0]} and now has ${characters[name].bullets} bullets!`);
            } else {
                console.log(`${name} doesn't have enough bullets to shoot at ${args[0]}!`);
            }

        } else if (command === 'TakeHit') {
            let damage = Number(args[0])
            let attacker = args[1]
            characters[name].hp -= damage
            if (characters[name].hp > 0) {
                console.log(`${name} took a hit for ${damage} HP from ${attacker} and now has ${characters[name].hp} HP!`);
            } else {
                delete characters[name]
                console.log(`${name} was gunned down by ${attacker}!`);
            }

        } else if (command === 'Reload') {
            if (characters[name].bullets < 6) {
                let difference = 6 - characters[name].bullets
                characters[name].bullets = 6
                console.log(`${name} reloaded ${difference} bullets!`);
            } else if (characters[name].bullets === 6) {
                console.log(`${name}'s pistol is fully loaded!`);
            }

        } else if (command === 'PatchUp') {
            let amount = Number(args[0])
            if (characters[name].hp >= 100) {
                console.log(`${name} is in full health!`);
            } else {
                let initialHp = characters[name].hp
                characters[name].hp = Math.min(characters[name].hp + amount, 100)
                let healedAmount = characters[name].hp - initialHp;
                console.log(`${name} patched up and recovered ${healedAmount} HP!`);
            }
        }
        commandLine = inputPosses.shift()
    }
    for (let char in characters) {
        console.log(`${char}\n HP: ${characters[char].hp}\n Bullets: ${characters[char].bullets}`);
    }
}
// solve((["2",

//     "Gus 100 0",
    
//     "Walt 100 6",
    
//     "FireShot - Gus - Bandit",
    
//     "TakeHit - Gus - 100 - Bandit",
    
//     "Reload - Walt",

//     "Ride Off Into Sunset"]))



// solve((["2",

//     "Jesse 100 4",
    
//     "Walt 100 5",
    
//     "FireShot - Jesse - Bandit",
    
//     "TakeHit - Walt - 30 - Bandit",
    
//     "PatchUp - Walt - 20" ,
    
//     "Reload - Jesse",
    
//     "Ride Off Into Sunset"]))


solve((["2",

    "Gus 100 4",
    
    "Walt 100 5",
    
    "FireShot - Gus - Bandit",
    
    "TakeHit - Walt - 100 - Bandit",
    
    "Reload - Gus",
    
    "Ride Off Into Sunset"]))