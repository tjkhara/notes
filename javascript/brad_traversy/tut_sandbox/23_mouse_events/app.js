const clearBtn = document.querySelector('.clear-tasks')
const card = document.querySelector('.card')
const heading = document.querySelector('h5')

// Click
// clearBtn.addEventListener('click', runEvent)

// Double click
// clearBtn.addEventListener('dblclick', runEvent)

// Mouse down
// clearBtn.addEventListener('mousedown', runEvent)

// Mouse up
// clearBtn.addEventListener('mouseup', runEvent)

// Mouse enter
card.addEventListener('mouseenter', runEvent)

// Event handler
function runEvent(e) {
  console.log(`Event type: ${e.type}`)
}