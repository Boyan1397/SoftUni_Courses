function convertToJson(firstName, lastName, hairColor) {
    let personObject = {
        name: firstName,
        lastName,
        hairColor,
    }
    
    let data = JSON.stringify(personObject)
    console.log(data);
}

convertToJson('George', 'Jones', 'Brown')