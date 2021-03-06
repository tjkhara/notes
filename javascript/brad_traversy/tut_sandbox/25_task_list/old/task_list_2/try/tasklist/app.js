// Define UI Vars
const form = document.querySelector('#task-form');
const taskList = document.querySelector('.collection');
const clearBtn = document.querySelector('.clear-tasks');
const filter = document.querySelector('#filter');
const taskInput = document.querySelector('#task');

// Load all event listeners
loadEventListeners();

// Load all event listeners
function loadEventListeners() {
  // Add task event
  form.addEventListener('submit', addTask);

  // Remove task event
  taskList.addEventListener('click', removeTask)

  // Clear task event
  clearBtn.addEventListener('click', clearTasks)

  // Filter task event
  filter.addEventListener('keyup', filterTasks)

}

// Add Task
function addTask(e) {
  if(taskInput.value === '') {
    alert('Add a task');
  }

  // Create li element
  const li = document.createElement('li');
  // Add class
  li.className = 'collection-item';
  // Create text node and append to li
  li.appendChild(document.createTextNode(taskInput.value));
  // Create new link element
  const link = document.createElement('a');
  // Add class
  link.className = 'delete-item secondary-content';
  // Add icon html
  link.innerHTML = '<i class="fa fa-remove"></i>';
  // Append the link to li
  li.appendChild(link);

  // Append li to ul
  taskList.appendChild(li);

  // Clear input
  taskInput.value = '';

  e.preventDefault();
}

// Remove task

function removeTask(e){
  if(e.target.parentElement.classList.contains('delete-item')){
    if(confirm('Are you sure?')){
      e.target.parentElement.parentElement.remove()
    }
  }
  
}

// Clear tasks

function clearTasks(e){
  taskList.innerHTML = ''
}

// Filter tasks
function filterTasks(e){
  const text = e.target.value.toLowerCase()

  // Select all lis
  lis = document.querySelectorAll(".collection-item")

  // loop through the lis
  lis.forEach(function(task){
    // Grab the text content of the first child
    const item = task.firstChild.textContent;
    // If the char being types in is in the item
    if(item.toLowerCase().indexOf(text) != -1){
      // Display the task (li)
      task.style.display = 'block'
    } else {
      task.style.display = 'none'
    }
  })
}
