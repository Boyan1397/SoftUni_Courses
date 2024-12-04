class Car {
    constructor(Brand, Model, Engine) {
        this.Brand = Brand
        this.Model = Model
        this.Engine = Engine
    }

    startIt(name) {
        console.log(`${name} started the brand new ${this.Brand}`);
        
    }
}

const car = new Car('Mercedes', 'GLE350DE', '3L')
console.log(car);
console.log(car.Brand);

car.startIt('Bobo')



class Hotel {
    constructor(Name, Stars) {
        this.Name = Name
        this.Stars = Stars
    }

    inFront(mycar) {
        console.log(`${mycar.Brand} in front of ${this.Name}`);
        
    }
}

let hotel1 = new Hotel('Europe', '4 Stars')
console.log(hotel1.Stars);

hotel1.inFront(car)