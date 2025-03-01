// Student Name: Kamal Dhital
// University ID: 2407046

//---------------------------------------------------------------------------------------------
//>>>>>>>>>>>>>Table of Content<<<<<<<<<<<<<
//---------------------------------------------------------------------------------------------
// 1. Declaration of block-scoped variable
// 2. Declaration and assigning the selector in the variable
//-----------------------------------------------------------------------------------------------
//    For Search City
//---------------------------------------------------------------------------------------------
// 3. Using Async Function and Fetching the data for search City Data Display
// 4. Function to get background image based on weather condition for search city
// 5. Calling the function of background image
// 6. Converting the time into local format
// 7. Event Handling and Calling the function of search City when user click search button
//------------------------------------------------------------------------------------------------
//   For Default City
//------------------------------------------------------------------------------------------------
// 8. Fetching the data and catching the error
// 9. Function to run background image based on weather condition for default city
// 10. Calling the function of background image
// 11. Converting time into local time
// 12. Catching the error
//-------------------------------------------------------------------------------------------------

// ! Declaration and assigning the selector in the variable
let mainBody = document.querySelector("#mainBody");
const weatherIcon = document.querySelector("#weatherIcon");
const temp = document.querySelector("#temperature");
const weatherCondition = document.querySelector("#weatherCondition");
const city = document.querySelector("#city");
const dateAndTime = document.querySelector("#dateAndTime");
const itFeelsLike = document.querySelector("#itFeelsLike");
const weatherDescription = document.querySelector("#weatherDescription");
const pressure = document.querySelector("#pressure");
const windSpeed = document.querySelector("#windSpeed");
const humidity = document.querySelector("#humidity");
const visibility = document.querySelector("#visibility");
const tableBody = document.querySelector("#weatherTable tbody");
const searchBar = document.querySelector("#searchInput");
const searchButton = document.querySelector("#searchButton");

function getBackgroundImage(data) {
  if (data[0].iconid >= 200 && data[0].iconid < 300) {
    mainBody.style.backgroundImage = `url("https://images.unsplash.com/photo-1511289081-d06dda19034d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fHw%3D")`;
  } else if (data[0].iconid >= 300 && data[0].iconid < 400) {
    mainBody.style.backgroundImage = `url("https://wallpapercave.com/wp/Z0kmvgB.jpg")`;
  } else if (data[0].iconid >= 500 && data[0].iconid < 600) {
    mainBody.style.backgroundImage = `url("https://th.bing.com/th/id/OIP.AVJXCd_GAKMrrk39l5OxTgHaEo?rs=1&pid=ImgDetMain")`;
  } else if (data[0].iconid >= 600 && data[0].iconid < 700) {
    mainBody.style.backgroundImage = `url("https://c4.wallpaperflare.com/wallpaper/230/80/44/branches-winter-snow-5k-snowfall-wallpaper-preview.jpg")`;
  } else if (data[0].iconid >= 700 && data[0].iconid < 800) {
    mainBody.style.backgroundImage = `url("https://live.staticflickr.com/6209/6087695435_4b545db144_b.jpg")`;
  } else if (data[0].iconid == 800) {
    mainBody.style.backgroundImage = `url("https://wallpapers.com/images/hd/bluish-orange-clear-sky-ckcbv6yqvjhcbi09.jpg")`;
  } else if (data[0].iconid >= 801 && data[0].iconid < 810) {
    mainBody.style.backgroundImage = `url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTocgXUMba2p6YV_X2BQkJhxwkUyp4GRGS35Q&usqp=CAU")`;
  }
}

function convertDateAndTime(timestamp) {
  const newdateAndTime = new Date(timestamp * 1000).toLocaleDateString(
    "en-US",
    {
      weekday: "short",
      day: "numeric",
      month: "short",
      year: "numeric",
    }
  );
  return newdateAndTime;
}

function filterDataForLast7Days(data) {
  if (typeof data !== "object" || data === null) {
    console.error("Input data is not an object.");
    return {};
  }

  const today = new Date();
  const sevenDaysAgo = new Date(today);
  sevenDaysAgo.setDate(today.getDate() - 7);

  const filteredData = {};

  for (const key in data) {
    if (data[key] || data[key].dt) {
      const itemDate = new Date(data[key].dt * 1000); // Assuming 'dt' is in seconds
      if (itemDate >= sevenDaysAgo || itemDate <= today) {
        filteredData[key] = data[key];
      }
    }
  }

  return filteredData;
}

function updateWeatherTable(filteredData) {
  tableBody.innerHTML = ""; // Clear existing content

  for (let i = 0; i < 7; i++) {
    const row = document.createElement("tr");
    row.innerHTML = generateContainerHTML(i, filteredData);
    tableBody.appendChild(row);
  }
}
function generateContainerHTML(index, data) {
  if (data[index]) {
    const formattedDate = convertDateAndTime(data[index].dt);
    return `
      <td>${formattedDate}</td>
      <td>${data[index].temp}°C</td>
      <td>${data[index].description}</td>
      <td>${data[index].feels_like}°C</td>
      <td>${data[index].pressure}hPa</td>
      <td>${data[index].windspeed}m/s</td>
      <td>${data[index].humidity}%</td>
      <td>${data[index].visibility}Km</td>
    `;
  } else {
    return "<td colspan='8'>No History Available</td>";
  }
}

// Using Async Function for Search City Data Display
async function getCurrentWeatherData(searchCity) {
  try {
    const response = await fetch(
      `http://localhost/main.php?history=true&city=${searchCity}`
    );
    if (!response.ok) {
      throw new Error(`City not found: ${searchCity}`);
    }

    const data = await response.json();
    console.log(data);

    // Writing the fetch data in HTML Page
    weatherIcon.innerHTML = `<img src = https://openweathermap.org/img/wn/${data[0].weathericon}@2x.png>`;
    temp.innerHTML = `${Math.round(data[0].temp)}°C`;
    weatherCondition.innerHTML = `${data[0].weather_condition}`;
    city.innerHTML = `${data[0].city}, ${data[0].country}`;
    itFeelsLike.innerHTML = `${data[0].feels_like}°C`;
    weatherDescription.innerHTML = `${data[0].description}`;
    pressure.innerHTML = `${data[0].pressure}<br>hPa`;
    windSpeed.innerHTML = `${data[0].windspeed}<br>m/s`;
    humidity.innerHTML = `${data[0].humidity}<br>%`;
    visibility.innerHTML = `${data[0].visibility}<br>Km`;

    getBackgroundImage(data);

    dateAndTime.innerHTML = convertDateAndTime(data[0].dt);
    const filteredData = filterDataForLast7Days(data);
    updateWeatherTable(filteredData);
  } catch (error) {
    console.error(error.message);
    alert(`City not found: ${searchCity}. Please enter a valid city name.`);
  }
}

searchButton.addEventListener("click", (event) => {
  event.preventDefault();
  getCurrentWeatherData(searchBar.value);
});

// Fetching the data and catching the error
fetch(`http://localhost/main.php?history=true&city=serampore`)
  .then((response) => response.json())
  .then((data) => {
    // Writing the fetch data in HTML Page
    weatherIcon.innerHTML = `<img src = https://openweathermap.org/img/wn/${data[0].weathericon}@2x.png>`;
    temp.innerHTML = `${Math.round(data[0].temp)}°C`;
    weatherCondition.innerHTML = `${data[0].weather_condition}`;
    city.innerHTML = `${data[0].city}, ${data[0].country}`;
    itFeelsLike.innerHTML = `${data[0].feels_like}°C`;
    weatherDescription.innerHTML = `${data[0].description}`;
    pressure.innerHTML = `${data[0].pressure}<br>hPa`;
    windSpeed.innerHTML = `${data[0].windspeed}<br>m/s`;
    humidity.innerHTML = `${data[0].humidity}<br>%`;
    visibility.innerHTML = `${data[0].visibility}<br>Km`;

    // Calling the function of background image
    getBackgroundImage(data);
    dateAndTime.innerHTML = convertDateAndTime(data[0].dt);
    const filteredData = filterDataForLast7Days(data);
    updateWeatherTable(filteredData);
  })
  // Catching the error
  .catch((error) => {
    console.log(
      "Unable to fetch the data!!! Please try again after a while.",
      error
    );
  });

// End of JS Code for Prototype 1
