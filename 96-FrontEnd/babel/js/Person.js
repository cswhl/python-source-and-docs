class Person {
    constructor (fullName, favColor) {
        this.name = fullName;
        this.favouriteColor = favColor;
        this.greet()
    }

    greet() {
        console.log('Hi There', this.name + this.favouriteColor)
    }
}

export default Person
