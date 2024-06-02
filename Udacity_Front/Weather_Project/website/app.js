/* Global Variables */
// Api url
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather?zip='
const apiKey = 'c32f7d82cb7e51cc3405c3472dcf5412'
const apiLink = '&units=Metric'
const postUrl = 'http://localhost:8000/add'
const getUrl = 'http://localhost:8000/all'
// Elements from index.html
const zip = document.getElementById('zip')
const feelings = document.getElementById('feelings')
const generate = document.getElementById('generate')
const dateBox = document.getElementById('date')
const tempBox = document.getElementById('temp')
const contentBox = document.getElementById('content')

/*
  1. Fetch the data from openweatherapi
  2. post the data to the server.js
  3. get the data from the sever and insert into html
*/
// Create a new date instance dynamically with JS
let d = new Date();
let newDate = (d.getMonth()+1)+'.'+ d.getDate()+'.'+ d.getFullYear();

// Received weather information from openweathermap apis
const getWeather = async (url,zip,apiKey) => {
  const weatherUrl = `${url}${zip},us&appid=${apiKey}${apiLink}`
  const response = await fetch(weatherUrl);
  try{
    const allData = await response.json();
    return allData;
  } catch(error){
    console.log("error",error);
  }
}

// Async POST
const postData = async (url, data = {})=>{
  const response = await fetch(url,{
    method : 'POST',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(data),
  });
  try {
    const newData = await response.json();
    return newData;
  } catch(error){
    console.log("error",error);
  }
}

// Insert post data into html
const upDate = async (url) => {
  const res = await fetch(url);
  try{
    const data = await res.json();
    dateBox.innerHTML = `Date: ${data.date}`
    tempBox.innerHTML = `Temperature: ${data.temperature}`
    contentBox.innerHTML = `Feeling: ${data.feelings}`
  } catch(error) {
    console.log("error",error);
  }
}

// Callback function generate entry
const entry = async () => {
  if (zip.value) {
    const weatherData = await getWeather(apiUrl,zip.value,apiKey)
    // https://openweathermap.org/current - JSON data example
    const data = {
      date: newDate,
      temperature: weatherData.main.temp,
      feelings: feelings.value
    }
    postData(postUrl,data);
    upDate(getUrl);
  } else{
    console.log("The zipcode is wrong");
  }
}

// Add event listener to click and generate
generate.addEventListener('click', entry)
