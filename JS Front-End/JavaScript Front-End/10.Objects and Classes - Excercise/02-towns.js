// function printTownInfo(locations) {
//     let locationsData = []
//     for (let location of locations) {
//         let [town, latitude, longitude] = location.split(' | ')

//         latitude = Number(latitude)
//             .toFixed(2)
//             .toString();

//         longitude = Number(longitude)
//         .toFixed(2)
//         .toString();
        
//         locationsData.push({
//             town,
//             latitude,
//             longitude,
//         }
//         )
//     }

//     locationsData.forEach(loc => console.log(loc)
//     )
// }

// printTownInfo(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625'])

// function fancySolve(dataArr) {
//     dataArr = dataArr.map(data => {
//         let [town, latitude, longitude] = data.split(' | ')
//         let locationsData = {
//             town,
//             latitude: Number(latitude).toFixed(2),
//             longitude: Number(longitude).toFixed(2),
//         }
//         return locationsData
//     })
    
//     dataArr.forEach(obj => {
//         console.log(obj);
//     });  
// }

// fancySolve(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);

function fancierSolve(dataArr) {
    dataArr = dataArr.map(row => row.split(' | '))
    dataArr = dataArr.map(([town, latitude, longitude]) => ({
        town,
        latitude: Number(latitude).toFixed(2),
        longitude: Number(longitude).toFixed(2),
    }))

    dataArr.forEach(obj => 
        {console.log(obj);
    });
    
}

fancierSolve(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);