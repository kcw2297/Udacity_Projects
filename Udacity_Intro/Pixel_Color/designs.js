// Varaibles for each id, this varaibles will be used for event listener
const color = document.getElementById('colorPicker'); // Color picked from user
const size = document.getElementById('sizePicker'); // Size of Grid
const grid = document.getElementById('pixelCanvas'); // Where the Grid appear
const img = document.getElementById("imgPicker"); // Img appear

// Add events on action by user
size.addEventListener("submit", makeGrid); // Call makeGrid function when user submit
grid.addEventListener("click",changeColor); // Call changeColor function when user click grid
img.addEventListener("click",imgPop);


// Make a grid base on the width and height
function makeGrid(event) {
  event.preventDefault(); // Prevent event default
  grid.innerHTML=""; // Delete the existing grid

  let height = document.getElementById('inputHeight').value; // Height from user pick
  let width = document.getElementById('inputWidth').value; // Width from user pick

// Nested for loop to make grid
  for(var y=0; y<height; y++){
    var table = document.createElement("tr");

    for(var x=0; x<width; x++){
      var row = document.createElement("td");
      table.appendChild(row);
    }
    grid.appendChild(table);
  }
};


tdCheck = event.target.nodeName.toLowerCase() ==="td"
backColor = event.target.style.background

// Change the color base on user picke
function changeColor(event){
  if(tdCheck && backColor===color.value ){
    backColor = #ffffff;
  } else if (tdCheck) {
    backColor = color.value;
  }
};

// Adding images
document.getElementById('.cat').addEventListener('click', function(){
  document.getElementById('.container').style.transform = 'transform: translate(-100vw)'
});
document.getElementById('.bear').addEventListener('click', function(){
  document.getElementById('.container').style.transform = 'transform: translate(-200vw)'
});
