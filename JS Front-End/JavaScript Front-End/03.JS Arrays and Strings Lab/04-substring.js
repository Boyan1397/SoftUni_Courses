function getSubstring(string, start, count) {
    let end = count + start
    let subst = string.slice(start, end) 
    return subst
}

console.log(getSubstring('ASentence', 1, 8));
console.log(getSubstring('SkipWord', 4, 7));

console.log(getSubstring("HelloWorld", 2, 3));
