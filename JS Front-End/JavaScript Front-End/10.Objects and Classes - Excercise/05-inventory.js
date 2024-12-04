function fancySolve(input) {
    let heroes = input
        .map(hero => hero.split(' / '))
        .map(([Hero, level, items]) => ({Hero, level, items}) )
        .sort((a, b) => a.level - b.level)
        .forEach(hero => console.log(`Hero: ${hero.Hero}\nlevel => ${hero.level}\nitems => ${hero.items}`));
}

fancySolve(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])

// function printInventory(heroesArr) {
//     let heroesRegisterArr = []

//     for (let heroInfo of heroesArr) {
//         let [Hero, level, items] = heroInfo.split(' / ')
//         heroesRegisterArr.push({
//             Hero, 
//             level: Number(level),
//             items,
//         }
//         )
//     }

//     heroesRegisterArr
//         .sort((a, b) => a.level - b.level)
//         .forEach(heroObj => console.log(`Hero: ${heroObj.Hero}\nlevel => ${heroObj.level}\nitems => ${heroObj.items}`))
// }

// printInventory(['Isacc / 25 / Apple, GravityGun',
//                 'Derek / 12 / BarrelVest, DestructionSword',
//                 'Hes / 1 / Desolator, Sentinel, Antara'
//                 ])

