function convertToObject(data) {
    let personObject = JSON.parse(data)
    Object.keys(personObject).forEach(key => {
        console.log(`${key}: ${personObject[key]}`);
    });  
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')