// Book constructor
function Book(title, author, isbn) {
  this.title = title
  this.author = author
  this.isbn = isbn
}

// UI constructor
function UI() { }

// Add book to list
UI.prototype.addBookToList = function (book) {
  const list = document.getElementById('book-list')
  // Create a tr element
  const row = document.createElement('tr')
  // Insert cols
  row.innerHTML = `
    <td>${book.title}</td>
    <td>${book.author}</td>
    <td>${book.isbn}</td>
    <td><a href="" class="delete">X</a></td>
  `

  list.appendChild(row)

  // Add the item to local storage

  // Get books already in storage
  let books;

  if(localStorage.getItem('books') === null) {
    books = [];
  } else {
    books = JSON.parse(localStorage.getItem('books'));
  }

  // Add book object to books array
  books.push(book)
  // Add it to local storage
  localStorage.setItem(JSON.stringify('books'))
}

// Show alert
UI.prototype.showAlert = function(message, className){
  // Create a div
  const div = document.createElement('div')
  div.className = `alert ${className}`
  div.appendChild(document.createTextNode(message))
  // Insert in dom
  const container = document.querySelector("div.container")
  const form = document.querySelector("#book-form")
  container.insertBefore(div, form)

  // Disappear after 3 seconds
  setTimeout(function(){
    document.querySelector('.alert').remove()
  }, 3000)
}

// Delete book
UI.prototype.deleteBook = function(target){
  if(target.className === 'delete'){
    target.parentElement.parentElement.remove()
  }
}

// Clear Fields
UI.prototype.clearFields = function () {
  document.getElementById('title').value = '';
  document.getElementById('author').value = '';
  document.getElementById('isbn').value = '';
}

// Event listeners
document.getElementById('book-form').addEventListener('submit', function (e) {

  // Get form values
  const title = document.getElementById('title').value,
    author = document.getElementById('author').value,
    isbn = document.getElementById('isbn').value

  // Instantiate a book
  const book = new Book(title, author, isbn)

  // Instantiate a UI object
  const ui = new UI();

  // Validate
  if (title === '' || author === '' || isbn === '') {
    // Error alert
    ui.showAlert('Please fill in all fields', 'error')

  } else {
    // Add book to list
    ui.addBookToList(book)

    // Success
    ui.showAlert('book added', 'success')

    // Clear fields
    ui.clearFields();
  }



  e.preventDefault()
})

// Event listener for delete
document.getElementById('book-list').addEventListener('click', function(e){

  const ui = new UI()
  ui.deleteBook(e.target)
  // Success
  ui.showAlert('Book deleted', 'success')
  e.preventDefault()
})