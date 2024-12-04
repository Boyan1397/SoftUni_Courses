function makeDict(input) {
    let dictionary = {}
    let words = input.map(row => JSON.parse(row))
    for (let wordObj of words) {
        let word = Object.keys(wordObj)[0];
        dictionary[word] = wordObj[word]
    }
    
    dictionary = Object.entries(dictionary)
        .sort((a, b) => a[0].localeCompare(b[0]))
        .forEach(([term, describtion]) => console.log(`Term: ${term} => Definition: ${describtion}`)) 
}


makeDict([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}' ])