function getAndPrintKvps(cityObject) {
    for (let key of Object.keys(cityObject)) {
        console.log(`${key} -> ${cityObject[key]}`)
    }
}

getAndPrintKvps({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000",
})
    
