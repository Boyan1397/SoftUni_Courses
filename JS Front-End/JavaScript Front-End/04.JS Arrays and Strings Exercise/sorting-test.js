function sorting(array) {
    console.log(array.sort((a, b) => {
        // ascending
        if (a < b) return -1; 
        if (a > b) return 1;
        return 0;
    }));
    
}

sorting([1, 44, 64, 4, 2, 8])


// sort numbers the best way
function bestSort(array2) {
    console.log(array2.sort((a, b) => b - a));
    
}

bestSort([4, 7, 3, 33, 22, 1, 567, 4])


// sort string alphabetically
function sortStrings(stringArr) {
    console.log(stringArr.sort((a, b) => b.localeCompare(a)));
    
}

sortStrings(['Banana', 'apple', 'cherry', 'date', 'banana'])