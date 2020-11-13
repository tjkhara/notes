pets = [
  {
    name: "Meowsalot",
    species: "Cat",
    age: 2
  },
  {
    name: "Barksalot",
    species: "Dog",
    age: 3
  },
  {
    name: "Purrsloud",
    species: "Cat",
    age: 8
  }
]

// Mutating
x = pets.push({
  name: "puppster",
  species: "dog",
  age: 1
})

// console.log(x)

// console.log(pets)

// map

// names = pets.map(nameOnly)

// function nameOnly(x){
//   return x.name
// }

// console.log(names)

// Filter

young = pets.filter(filterYoung)

function filterYoung(x){
  return x.age < 4
}

console.log(young)