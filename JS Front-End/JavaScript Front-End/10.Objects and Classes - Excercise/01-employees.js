// long
// function printEmployeesInfo(namesArr) {
//     let employeeDataObj = {}
    
//     namesArr.forEach(name => {
//         employeeDataObj[name] = name.length
//     });
    
//     for (let empName in employeeDataObj) {
//         console.log(`Name: ${empName} -- Personal Number: ${employeeDataObj[empName]}`);  
//     } 
// }

// short
// function printEmployeesInfo(namesArr) {
//     let employees = namesArr.map(name => {
//         let employee = {
//             name,
//             personalNumber: name.length,
//         }
//         return employee
//     }) 
    
//     for(let data of employees) {
//         console.log(`Name: ${data.name} -- Personal Number: ${data.personalNumber}`); 
//     } 
// }

// shortest
function printEmployeesInfo(namesArr) {
    let employees = namesArr.map(name => ({name, personalNumber: name.length})) 
    
    for(let data of employees) {
        console.log(`Name: ${data.name} -- Personal Number: ${data.personalNumber}`); 
    } 
}


printEmployeesInfo(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal'])