<?php


// Name : Kamal Dhital
// University Student Number : 2407046


// * Defining servername, username and password for localhost connection
$serverName = "localhost";
$userName = "root";
$password = "";


// ! Providing city as a query in url to get the data according to desired city by default it will be "Serampore"


$city = isset($_GET['city']) ? $_GET['city'] : "Serampore";


// ! Function to create database and table only create if not exists

function creatingDatabaseAndTable($conn)
{
    // * Funciton to create the database and table only if not exists
    try {
        $conn->query("create database if not exists Weather");
        $conn->select_db("Weather");
        $conn->query("create table if not exists WeatherRecords(
        dt int,
        city varchar(20),
        country varchar(50),
        weathericon char(50),
        iconid int,
        temp double,
        weather_condition varchar(50),
        description varchar(50),
        feels_like double,
        pressure int,
        windspeed double,
        humidity int,
        visibility int)");
        if ($conn) {
            return $conn;
        } else {
            return false;
        }
    } catch (Exception $err_mesg) {
        echo "Error while connection to database" . $err_mesg;
    }
}

// ! Function to connect with the local server 

function connectingServer($serverName, $userName, $password)
{
    // * Function to connect to local server and return the connection
    try {
        $connection = new mysqli($serverName, $userName, $password);
        if ($connection) {
            return creatingDatabaseAndTable($connection);
        } else {
            echo "Error in establishing the connection.";
        }
    } catch (Exception $err_mesg) {
        echo "Error in connecting to the server: " . $err_mesg;
    }
}



// ! Function to Fetch Data from OpenMapWeather with passing the city parameter

function fetchingDataFromAPI($city)
{
    // * Function to fetch data from the OpenWeatherMap and return the decode value
    try {
        $API_KEY = "1b7dd59820bd992941b5134e6aed93c8";
        $fetch_url = 'http://api.openweathermap.org/data/2.5/weather?q=' . $city . '&appid=' . $API_KEY . '&units=metric';
        // ! file_get_contents is used to fetch the data in php 
        $fetchData = file_get_contents($fetch_url, true);
        $decodeFetchData = json_decode($fetchData, true);
        if ($decodeFetchData) {
            return $decodeFetchData;
        } else {
            return false;
        }
    } catch (Exception $err_mesg) {
        echo 'Error in fetching data from api key' . $err_mesg;
    }
}

// ! Function to insert data into database which is already fetch from the OpenWeatherMap

function insertingDataIntoDatabase($connection, $city, $data)
{
    // * Function to insert the data fetch from the database and return the value after inserting
    try {
        $dt = $data['dt'];
        $city = $data['name'];
        $country = $data['sys']['country'];
        $weathericon = $data['weather'][0]['icon'];
        $iconid = $data['weather'][0]['id'];
        $temp = $data['main']['temp'];
        $weather_condition = $data['weather'][0]['main'];
        $description = $data['weather'][0]['description'];
        $feels_like = $data['main']['feels_like'];
        $pressure = $data['main']['pressure'];
        $windspeed = $data['wind']['speed'];
        $humidity = $data['main']['humidity'];
        $visibility = $data['visibility'];

        $connectingToTable = $connection->query('insert into WeatherRecords(dt, city, country, weathericon, iconid, temp, weather_condition, description, feels_like, pressure, windspeed, humidity, visibility)values(
            ' . $dt . ',
            "' . $city . '",
            "' . $country . '",
            "' . $weathericon . '",
            ' . $iconid . ',
            ' . $temp . ',
            "' . $weather_condition . '",
            "' . $description . '",
            ' . $feels_like . ',
            ' . $pressure . ',
            ' . $windspeed . ',
            ' . $humidity . ',
            ' . $visibility . ')');
        if ($connectingToTable) {
            return $connectingToTable;
        } else {
            return false;
        }
    } catch (Exception $err_mesg) {
        echo 'Error while inserting data into database' . $err_mesg;
    }
}

// ! Function to extract data from database and return the encode data and takes connection and city parameter

function extractingDataFromDatabase($connection, $city)
{
    // * Try to extract all the data from the database and encode it then return the encoded value and catch the exception if araise
    try {
        $selectingFromDatabase = $connection->query('select * from weatherrecords where city ="' . $city . '" ORDER BY dt DESC');
        if ($selectingFromDatabase) {
            $fetchSelectedData = $selectingFromDatabase->fetch_all(MYSQLI_ASSOC);
            $selectedData = json_encode($fetchSelectedData);
            return $selectedData;
        } else {
            return false;
        }
    } catch (Exception $err_mesg) {
        echo 'Error in extracting data from database' . $err_mesg;
    }
}

// ! Function to fetch and insert data with connection and city parameter

function fetchAndInsert($connection, $city)
{
    // * Function which include the other function and this function is used in logic this function fetch the data, insert it into database and extract from the database and return the value
    try {
        // Fetch the data from api
        $newFetchData = fetchingDataFromAPI($city);
        // * Checking Fetch data
        if ($newFetchData) {
            // Insert the data to database
            $insertIntoDatabase = insertingDataIntoDatabase($connection, $city, $newFetchData);
            // * Checking Inserting Data
            if ($insertIntoDatabase) {
                // Extract the data from database
                $newExtractingData = extractingDataFromDatabase($connection, $city);
                // Decoding the data
                $newExtractingData = json_decode($newExtractingData, true);
                // * Checking extracting data
                if ($newExtractingData) {
                    return $newExtractingData;
                } else {
                    // Catching Error while extracting data
                    return false;
                }
            } else {
                // Catching Error while inserting data
                echo json_encode(["error" => "Error on inserting data"]);
            }
        } else {
            // Catching Error while fetching data
            echo json_encode(["error" => "Error on fetching data"]);
        }
    } catch (Exception $err_mesg) {
        // Catching Exception
        echo json_encode(["error" => "Error on fetchAndInsert", "" => $err_mesg]);
    }
}