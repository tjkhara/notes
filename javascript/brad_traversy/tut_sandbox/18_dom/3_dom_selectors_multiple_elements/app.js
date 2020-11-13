// document.getElementsByClassName

const items = document.getElementsByClassName('collection-item')

console.log(items)
console.log(items[0])

items[0].getElementsByClassName.color = 'red'
items[3].getElementsByClassName.color = 'Hello'

// Narrow scope

const listItems = document.querySelector('ul').getElementsByClassName('collection-item');