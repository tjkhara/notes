const form = document.getElementById("task-form")
const taskList = document.querySelector("ul.collection")
const clearBtn = document.querySelector(".clear-tasks")
const filter = document.getElementById("filter")
const taskInput = document.getElementById("task")

function loadEventListeners(){
  form.addEventListener("submit", addTask)
}

loadEventListeners();

function addTask(e){
  if(taskList.value === ''){
    alert('Add a task')
  }

  // Create li
  const li = document.createElement('li')
  // Add class
  li.className = 'collection-item'

  // Create text node
  const textNode = document.createTextNode(taskInput.value)

  // Create text node and append it to li
  li.appendChild(textNode)

  // Create new link element
  const link = document.createElement('a')

  // Add class
  link.className = 'delete-item secondary-content'

  // The the icon html
  link.innerHTML = '<i class="fa fa-remove"></i>'

  // Append link to li
  li.appendChild(link)

  // Append li to ul
  taskList.appendChild(li)

  // Clear input
  taskInput.value = ''

  e.preventDefault()
}
