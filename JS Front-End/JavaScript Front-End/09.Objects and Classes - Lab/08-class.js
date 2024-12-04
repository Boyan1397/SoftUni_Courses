function solve(catsArray) {
    class Cat {
        constructor (name, age) {
            this.name = name
            this.age = age
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);    
        }
    }

    for (let cat of catsArray) {
        let [name, age] = cat.split(' ')
        let myCat = new Cat(name, age)
        myCat.meow()
    }
}

solve(['Mellow 2', 'Tom 5'])