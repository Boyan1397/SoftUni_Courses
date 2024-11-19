function splitWords(text) {
    let matches = text.matchAll(/[A-Z][a-z]*/g)
    let result = []
    for (let match of matches) {
        result.push(match[0])
    }
    console.log(result.join(', '));
}

splitWords('SplitMTeIfYouCanHaHaYouCantOrYouCan')
splitWords('HoldTheDoor')
splitWords('ThisIsSoAnnoyingToDo')