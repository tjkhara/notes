// Anonymous functions

let myNumbers = [10, 500, 2000]

// Use map to create a new array where each item from this array has been doubled

// function doubleMe(x){
//     return 2*x
// }

let doubles = myNumbers.map(x => 2*x)
console.log(doubles)