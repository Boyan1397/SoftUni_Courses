function solve() {
    let thHeadingElements = document.querySelectorAll('thead th');
    let tRowElements = document.querySelectorAll('tbody tr')
    let outputArea = document.getElementById('output')
    
    let columns = Array
        .from(thHeadingElements)
        .map(thElement => {
            let inputElement = thElement.querySelector('input')

            return {
                name: thElement.textContent.trim().toLowerCase(),
                active: inputElement.checked
            }
        });
    
    let finalResult = Array
        .from(tRowElements)
        .map(rowElement => {
            let tdElements = rowElement.querySelectorAll('td')
            
            return Array
                .from(tdElements)
                .reduce((rowData, tdElement, i) => {
                    if (!(columns[i].active)) {
                        return rowData
                    }

                    let name = columns[i].name
                    rowData[name] = tdElement.textContent

                    return rowData
                } , {})
            
        });
    
    outputArea.value = JSON.stringify(finalResult, null, 2)
    
}

