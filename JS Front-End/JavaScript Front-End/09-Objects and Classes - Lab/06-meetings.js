function menageMeetings(meetingsArray) {
    let daysCounterObj = {}
    let succesfullMeetingsObject = {}

    meetingsArray.forEach(pair => {
        pair = pair.split(' ')

        if (daysCounterObj[pair[0]]) {
            console.log(`Conflict on ${pair[0]}!`);    
        } else {
            daysCounterObj[pair[0]] = 1
            console.log(`Scheduled for ${pair[0]}`);
            succesfullMeetingsObject[pair[0]] = pair[1]
        }
    });
    
    for (let day in succesfullMeetingsObject) {
        console.log(`${day} -> ${succesfullMeetingsObject[day]}`);   
    } 
}

menageMeetings(['Monday Peter', 'Wednesday Bill', 'Monday Tim', 'Friday Tim'])
// menageMeetings(['Friday Bob', 'Saturday Ted', 'Monday Bill', 'Monday John', 'Wednesday George'])