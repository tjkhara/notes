const person = {
  firstName: 'Steve',
  age: 30,

  getBirthYear: function(){
    return 2017 - this.age
  }
}

console.log(person.getBirthYear())