document.querySelector('form').addEventListener('submit', function(e){
  
  const task = document.getElementById("task").value;

  if(localStorage.getItem('tasks') == null){
    tasks = [task]
  } else {
    tasks = JSON.parse(localStorage.getItem('tasks'))
    tasks.push(task)
  }

  localStorage.setItem('tasks', JSON.stringify(tasks))

  taskList = JSON.parse(localStorage.getItem('tasks'))

  console.log(taskList)

  e.preventDefault()
})