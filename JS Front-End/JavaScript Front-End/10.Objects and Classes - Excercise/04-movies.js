function moviesJson(moviesArr) {
    let moviesData = []
    for (let movie of moviesArr) {
        if (movie.includes('addMovie')) {
            let movieName = movie.split('addMovie ').join('')
            moviesData.push({
                name: movieName,
            })            
        } else if (movie.includes('directedBy')) {
            let [name, director] = movie.split(' directedBy ')

            let movieObj = moviesData.find(movie =>  movie.name === name)
            if (movieObj) {
                movieObj.director = director
            }
            
        } else if (movie.includes('onDate')) {
            let [name, date] = movie.split(' onDate ')

            let movieObj = moviesData.find(movie => movie.name === name)
            if (movieObj) {
                movieObj.date = date
            }
        } 
    }

    moviesData
        .filter(movie => movie.name && movie.director && movie.date)
        .map(movie => JSON.stringify(movie))
        .forEach(movie => console.log(movie)
        )
    
}

moviesJson([

    'addMovie Fast and Furious',
    
    'addMovie Godfather',
    
    'Inception directedBy Christopher Nolan',
    
    'Godfather directedBy Francis Ford Coppola',
    
    'Godfather onDate 29.07.2018',
    
    'Fast and Furious onDate 30.07.2018',
    
    'Batman onDate 01.08.2018',
    
    'Fast and Furious directedBy Rob Cohen'
    
    ])