const name = "John"
const age = 30;
const job = "Web Developer";
const city = "Miami";
let html;


html = `

<ul>
  <li>${name}</li>
  <li>${age}</li>
  <li>${job}</li>
  <li>${city}</li>
</ul>

`;

document.body.innerHTML = html;