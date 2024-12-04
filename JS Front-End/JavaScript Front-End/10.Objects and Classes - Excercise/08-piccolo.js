function parkingLot(inputData) {
    let parking = {}
    for (let row of inputData) {
        let [command, number] = row.split(', ')
        if (command === 'IN') {
            parking[number] = true
        } else if (command === 'OUT') {
            delete parking[number]
        }
    }

    parking = Object.keys(parking).sort() 
    if (parking.length === 0) {
        console.log('Parking Lot is Empty')
    } else {
        console.log(parking.join('\n'))
    }
}

parkingLot(['IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA', 'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 'IN, CA2822UU'])