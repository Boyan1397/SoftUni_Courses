function ticketPricing(day, age) {
    let price;
    if (0 <= age && age <= 18) {
        switch(day) {
            case 'Weekday':
                price = '12$';
                break;
            case 'Weekend':
                price = '15$';
                break;
            case 'Holiday':
                price = '5$'
                break
        }
    } else if (18 < age && age <= 64) {
        switch(day) {
            case 'Weekday':
                price = '18$';
                break;
            case 'Weekend':
                price = '20$';
                break;
            case 'Holiday':
                price = '12$'
                break
        }
    } else if (64 < age && age <= 122) {
        switch(day) {
            case 'Weekday':
                price = '12$';
                break;
            case 'Weekend':
                price = '15$';
                break;
            case 'Holiday':
                price = '10$'
                break
        }
    } else {
        price = 'Error!'
        
    }

    console.log(price)
}



ticketPricing('Weekday', 42)
ticketPricing('Holiday', -12)
ticketPricing('Holiday', 15)