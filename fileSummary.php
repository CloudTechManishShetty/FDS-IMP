<?php

// Read file name from user
echo "Enter the file name: ";
$filename = trim(fgets(STDIN));

while (true) {
    echo "\nFile Operations Menu:\n";
    echo "1. Display file type\n";
    echo "2. Display last modification time\n";
    echo "3. Display file size\n";
    echo "4. Delete file\n";
    echo "5. Exit\n";

    echo "Enter your choice: ";
    $choice = trim(fgets(STDIN));

    switch ($choice) {
        case 1:
            displayFileType($filename);
            break;
        case 2:
            displayLastModificationTime($filename);
            break;
        case 3:
            displayFileSize($filename);
            break;
        case 4:
            deleteFile($filename);
            break;
        case 5:
            exit();
        default:
            echo "Invalid choice. Please choose again.\n";
    }
}

function displayFileType($filename) {
    if (file_exists($filename)) {
        echo "File type: " . mime_content_type($filename) . "\n";
    } else {
        echo "File not found.\n";
    }
}

function displayLastModificationTime($filename) {
    if (file_exists($filename)) {
        echo "Last modification time: " . date("Y-m-d H:i:s", filemtime($filename)) . "\n";
    } else {
        echo "File not found.\n";
    }
}

function displayFileSize($filename) {
    if (file_exists($filename)) {
        echo "File size: " . filesize($filename) . " bytes\n";
    } else {
        echo "File not found.\n";
    }
}

function deleteFile($filename) {
    if (file_exists($filename)) {
        if (unlink($filename)) {
            echo "File deleted successfully.\n";
        } else {
            echo "Error deleting file.\n";
        }
    } else {
        echo "File not found.\n";
    }
}

?>