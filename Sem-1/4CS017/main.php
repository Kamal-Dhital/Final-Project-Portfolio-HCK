<?php

// Name : Kamal Dhital
// University Student Number : 2407046

// * To give control access to another server from one server
header("Access-Control-Allow-Origin: *");


// * To change the content type in json format
header("Content-Type: application/json");


// * Including config.php file in this file
include('config.php');


// ! Calling function which contain connection to local server

$connection = connectingServer($serverName, $userName, $password);


// ! Refresh time for data
$refreshTime = 24 * 60 * 60;


// ! Extracting data from database and decode it
$allExtractingData = json_decode(extractingDataFromDatabase($connection, $city), true);


// ! Checking the extracting data whether it is enpty or not
if (!empty($allExtractingData)) {

    // * Checking whether history is passed or not
    if (isset($_GET["history"])) {

        // * Taking the latest data from the overall data and check its time 
        $extractingData = $allExtractingData[0];
        $dataTimeStamp = isset($extractingData['dt']) ? $extractingData['dt'] : 0;
        $currentTime = time();

        // * Checking whether latest data fetch time is greater than refresh time or not
        if ($currentTime - $dataTimeStamp > $refreshTime) {
            $newFetchData = fetchAndInsert($connection, $city);
            $lastIndex = count($newFetchData) - 1;
            $lastData = $newFetchData[$lastIndex];
            echo json_encode($lastData);
        } else {
            echo json_encode($allExtractingData);
        }

    } else {
        // * Executing this block if history is not passed by the user and doing as above
        $extractingData = $allExtractingData[0];
        $dataTimeStamp = isset($extractingData['dt']) ? $extractingData['dt'] : 0;
        $currentTime = time();
        if ($currentTime - $dataTimeStamp > $refreshTime) {
            $newFetchData = fetchAndInsert($connection, $city);
            $lastIndex = count($newFetchData) - 1;
            $lastData = $newFetchData[$lastIndex];
            echo json_encode($lastData);
        } else {
            // * Echo the last index data if history is not passed by user 
            echo json_encode($extractingData);
        }
    }
} else {

    // ! This block execute only when data is not available in the databasee
    $dataFromDatabase = fetchAndInsert($connection, $city);
    echo json_encode($dataFromDatabase);
}