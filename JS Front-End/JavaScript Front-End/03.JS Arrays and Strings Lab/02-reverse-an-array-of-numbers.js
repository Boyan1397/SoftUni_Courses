function reverseArray(n, array) {
    
    const result = array
        .slice(0, n)
        .reverse()
        .join(' ')

    return result
}

console.log(reverseArray(3, [10, 20, 30, 40, 50]));
