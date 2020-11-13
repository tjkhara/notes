let pets = [
    {name: "meow", species: "cat", age: 2},
    {name: "miles", species: "dog", age: 10},
    {name: "gogo", species: "mouse", age: 1},
    {name: "popo", species: "dog", age: 1}
]

// x = pets.push({name: "Puppster", species: "dog", age: 4})

// console.log(x)

// let y = pets.map(nameOnly)

function nameOnly(dict) {
    return dict["name"]
}

// console.log(y)

// filter

let dogs = pets.filter(onlyDogs)

function onlyDogs(x){
    return x.species == "dog"
}

// console.log(dogs)

function onlyBabies(x){
    return x.age < 3
}

let babies = pets.filter(onlyBabies)

// console.log(babies)

// Now to get only baby dogs

let babyDogNames = pets.filter(onlyDogs).filter(onlyBabies).map(nameOnly)

console.log(babyDogNames)