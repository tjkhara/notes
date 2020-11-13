// document.querySelector('.clear-tasks').addEventListener('click', function(e){
//   console.log('hello world')
//   e.preventDefault()
// })

// Putting a named function

document.querySelector('.clear-tasks').addEventListener('click', onClick)

function onClick(e){
  // console.log('Click')
  // e.preventDefault()

  let val;

  val = e
  

  // Event target element
  val = e.target;
  val = e.target.id;
  val = e.target.className;
  val = e.target.classList;

  e.target.innerText = "HEllo"

  // Event type
  val = e.type


  console.log(val)
}