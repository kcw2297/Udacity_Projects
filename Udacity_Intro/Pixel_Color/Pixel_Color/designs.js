`/**
* @description variable to count the grid
*/`
let funcCalled = 0;

/**
* @description variable to reference the table
*/
const table = document.getElementById("pixelCanvas");

/**
* @description Select color input
*/
let color = document.querySelector("#colorPicker");
color.addEventListener("change", function(event) {
  color.setAttribute('value',event.target.value);
});

/**
* @description Select height input
*/
let height = document.querySelector("#inputHeight");
 height.addEventListener("input", function(event) {
  height.setAttribute('value',event.target.value);
});

/**
* @description Select width input
*/
let width = document.querySelector("#inputWidth");
width.addEventListener("input", function(event) {
  width.setAttribute('value',event.target.value);
});

/**
* @description create a grid with chosen height and width
*/
function makeGrid() {
funcCalled += 1;
for(let height1 = height.value; height1> 0; --height1) {
    let row = document.createElement("tr")
    table.appendChild(row);
    for (let width1 = width.value; width1 > 0; --width1) {
        let column = document.createElement("td")
        row.appendChild(column);
      }
    };
};

/**
* @description remove the grid
*/
function removeGrid() {
  while (table.firstElementChild) {
    table.removeChild(table.firstElementChild);}
}

/**
* @description set/unset background color to the squares
*/
function colorCell() {
if (funcCalled > 0) {
    let cell = document.querySelectorAll("td");
    cell.forEach(function(el){el.addEventListener("click", function() {
      el.style.backgroundColor == false ?  el.style.backgroundColor = color.value : el.setAttribute("style","")
    })});
  }
};

/**
* @description prevent the submit button to refresh the page
*/
document.querySelector("#sizePicker").addEventListener("submit", function(event){
    event.preventDefault();
});
/**
* @description call makeGrid() and colorCell() and reset the grid if already exists
*/
document.querySelector("#sizePicker").addEventListener("submit", function(){
        if (funcCalled === 0) {
        makeGrid();
        colorCell();
      } else {
        removeGrid();
        makeGrid();
        colorCell();
      }
});
