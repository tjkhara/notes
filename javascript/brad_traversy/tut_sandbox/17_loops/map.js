const users = [
  {id: 1, name: 'John'},
  {id: 2, name: 'Karen'},
  {id: 3, name: 'Sarah'}
]

const ids = users.map(user => user.id)

console.log(ids)

// Full version

// const full_ids = users.map(function(user){
//   return user.id
// })
