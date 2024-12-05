function extract(content) {
    const myContent = document.getElementById(content);
    const regEx = /(?<=\()[^)]+(?=\))/g
    const matches = myContent.textContent.match(regEx);   
    console.log(matches.join('; '));
    
    return (matches.join('; '));
}