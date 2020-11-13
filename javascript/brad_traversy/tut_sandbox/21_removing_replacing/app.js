// Replace elements

// Create an element
const newHeading = document.createElement('h2')

// Add id
newHeading.id = 'task-title'

// Create new text node
newHeading.appendChild(document.createTextNode('Task List'))

// Get the old heading
const oldHeading = document.getElementById('task-title')

// Parent
const cardAction = document.querySelector('.card-action')

// Replace
cardAction.replaceChild(newHeading, oldHeading)


// Remove element
const lis = document.querySelectorAll('li')
const list = document.querySelector('ul')

// Remove specific list item
lis[0].remove();

// Remove child element
list.removeChild(lis[3])

// Classes and attributes
const firstLi = document.querySelector('li:first-child')
const link = firstLi.children[0]

let val;

val = link.className;
val = link.classList;
val = link.classList[0]
link.classList.add('test')
val = link

// Attributes
val = link.getAttribute('href')
val = link.setAttribute('href', 'http://google.com')
link.setAttribute('title', 'Google')
// val = link.hasAttribute('href');
val = link.removeAttribute('title')
val = link


console.log(val)