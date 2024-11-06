function solve(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0

    let helmets = 0
    let swords = 0
    let shields = 0
    let armors = 0
    for (let i = 1; i < lostFights + 1; i++) {
        if (i % 2 === 0) {
            expenses += helmetPrice;
            helmets += 1
        }

        if (i % 3 === 0) {
            expenses += swordPrice;
            swords += 1
        }

        if (i % 2 === 0 && i % 3 === 0 ) {
            expenses += shieldPrice
            shields += 1
        }

        if (shields % 2 === 0 && shields !== 0) {
            expenses += armorPrice
            armors += 1
            shields = 0
        }
    }
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

solve(7, 2, 3, 4, 5)

solve(23, 12.50, 21.50, 40, 200)