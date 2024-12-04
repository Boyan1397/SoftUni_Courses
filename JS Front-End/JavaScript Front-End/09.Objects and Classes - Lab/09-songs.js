function solve(dataArr) {
    class Song {
        constructor(name, time) {
            this.name = name
            this.time = time
        }
    }

    let nElements = dataArr.shift()
    let lastTypelist = dataArr.pop()
    let collections = {}
    let allSongs = []


    dataArr.forEach(line => {
        let [typeList, name, time] = line.split('_')
        if (!(collections[typeList])) {
            collections[typeList]= []
        };

        let song = new Song(name, time)
        collections[typeList].push(song)
        allSongs.push(song)
    });   
    
    if (lastTypelist === 'all') {
        allSongs.forEach(song => console.log(song.name))
    } else {
        collections[lastTypelist].forEach(song => console.log(song.name))
    }
}


solve([3, 'favourite_DownTown_3:14', 'favourite_Kiss_4:16', 'favourite_Smooth Criminal_4:01', 'all'])
solve([4,

    'favourite_DownTown_3:14',
    
    'listenLater_Andalouse_3:24',
    
    'favourite_In To The Night_3:58',
    
    'favourite_Live It Up_3:48',
    
    'listenLater'])