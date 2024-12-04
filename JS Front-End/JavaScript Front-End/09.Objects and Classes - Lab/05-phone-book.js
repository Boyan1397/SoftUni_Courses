function solve(bookArray) {
    let bookObject = {}
    
    bookArray.forEach(pair => {
        pair = pair.split(' ')
        bookObject[pair[0]] = pair[1]
    });
    
    for (let name in bookObject) {
        console.log(`${name} -> ${bookObject[name]}`);
        
    }
}

solve(['Tim 0834212554', 'Peter 0877547887','Bill 0896543112', 'Tim 0876566344'])
solve(['George 0552554', 'Peter 087587', 'George 0453112', 'Bill 0845344'])