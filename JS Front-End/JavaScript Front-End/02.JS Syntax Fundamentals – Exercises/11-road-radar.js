function roadRadar(speed, areaType) {
    let limit = 0;
    switch (areaType) {
        case ('motorway'):
            limit = 130;
            break;
        case ('interstate'):
            limit = 90;
            break;
        case ('city'):
            limit = 50;
            break;
        case ('residential'):
            limit = 20;
            break;
    }

    let difference = 0
    let status = ''
    if (speed <= limit) {
        console.log(`Driving ${speed} km/h in a ${limit} zone`);
    } else if (speed > limit) {
        difference = speed - limit
    
        if (speed <= (limit + 20)) {
            status = 'speeding'
        } else if (speed <= (limit + 40)) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${limit} - ${status}`);
        
    }
}

roadRadar(40, 'city')
roadRadar(21, 'residential')
roadRadar(120, 'interstate')
roadRadar(200, 'motorway')
