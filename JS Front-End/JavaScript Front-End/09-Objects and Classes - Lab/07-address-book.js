function sortBooks(dataArray) {
    let dataObject = {}
    // for (let pair of dataArray) {
    //     let [name, address] = pair.split(':')
    //     dataObject[name] = address
    // }
    
    dataObject = dataArray.reduce((book, line) => {
        let [name, address] = line.split(':')
        book[name] = address

        return book
    }, {})
    
    let sortedData = Object.entries(dataObject).sort((a, b) => a[0].localeCompare(b[0]))
    
    sortedData = Object.fromEntries(sortedData)
    for (let name in sortedData) {
        console.log(`${name} -> ${sortedData[name]}`);        
    }
}

sortBooks(['Tim:Doe Crossing', 'Bill:Nelson Place', 'Peter:Carlyle Ave', 'Bill:Ornery Rd'])