<?php

// Read file names from user
echo "Enter the source file name: ";
$sourceFile = trim(fgets(STDIN));

echo "Enter the destination file name: ";
$destinationFile = trim(fgets(STDIN));

// Check if source file exists
if (!file_exists($sourceFile)) {
    echo "Source file not found.\n";
    exit;
}

// Check if destination file exists
if (!file_exists($destinationFile)) {
    echo "Destination file not found. Creating a new file.\n";
    touch($destinationFile);
}

// Append content of source file to destination file
$fileContent = file_get_contents($sourceFile);
file_put_contents($destinationFile, $fileContent, FILE_APPEND);

echo "Content appended successfully.\n";

?>