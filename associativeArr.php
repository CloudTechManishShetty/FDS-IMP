<?php

// Initialize an empty associative array
$associativeArray = [];

// Check if form data is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize the associative array from form data
    $numElements = $_POST["numElements"];
    for ($i = 0; $i < $numElements; $i++) {
        $key = $_POST["key_" . $i];
        $value = $_POST["value_" . $i];
        $associativeArray[$key] = $value;
    }

    // Perform operation based on user choice
    $choice = $_POST["choice"];
    switch ($choice) {
        case 1:
            reverseKeyValuePairs($associativeArray);
            break;
        case 2:
            traverseRandomly($associativeArray);
            break;
        case 3:
            convertToVariables($associativeArray);
            break;
        case 4:
            displayElements($associativeArray);
            break;
        default:
            echo "Invalid choice. Please choose again.";
    }
}

function reverseKeyValuePairs(&$associativeArray) {
    // Reverses the order of each element's key-value pair.
    $reversedArray = array_flip($associativeArray);
    $associativeArray = $reversedArray;
    echo "Key-value pairs reversed successfully.<br>";
}

function traverseRandomly($associativeArray) {
    // Traverses the elements in the array in random order.
    $keys = array_keys($associativeArray);
    shuffle($keys);
    foreach ($keys as $key) {
        echo "$key: $associativeArray[$key]<br>";
    }
}

function convertToVariables($associativeArray) {
    // Converts the array elements into individual variables.
    extract($associativeArray);
    echo "Array elements converted to individual variables.<br>";
}

function displayElements($associativeArray) {
    // Displays the elements of the array along with keys.
    foreach ($associativeArray as $key => $value) {
        echo "$key: $value<br>";
    }
}

?>