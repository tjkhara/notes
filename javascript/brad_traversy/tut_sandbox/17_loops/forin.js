const user = {
  firstName: 'John',
  lastName: 'Smith',
  age: 32
}

for(let x in user){
  console.log(`${x} : ${user[x]}`)
}