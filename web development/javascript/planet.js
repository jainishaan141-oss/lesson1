class Planet{
    constructor(name, fact){
        this.fact = fact
        this.name = name
    }
    showInfo(){
        console.log("Planet:" , this.name)
        console.log("fact:" , this.fact)
    }
}
function showPlanet(){
    let earth = new Planet(
        "earth" ,
        "earth is the only known planet that supports life."
    )
     let mars = new Planet(
        "mars" ,
        "mars is the only known planet that supports life."
    )
     let jupiter = new Planet(
        "jupiter" ,
        "jupiter is the largest planet in the solar system."
    )
    earth.showInfo()
    mars.showInfo()
    jupiter.showInfo()
}
showPlanet()