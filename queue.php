<?php

$queue = [];

function enqueue(&$queue) {
    echo "Enter element to insert: ";
    $element = trim(fgets(STDIN));
    array_push($queue, $element);
    echo "Element inserted successfully.\n";
}

function dequeue(&$queue) {
    if (empty($queue)) {
        echo "Queue is empty.\n";
    } else {
        $removedElement = array_shift($queue);
        echo "Removed element: $removedElement\n";
    }
}

function displayQueue($queue) {
    if (empty($queue)) {
        echo "Queue is empty.\n";
    } else {
        echo "Queue elements: \n";
        foreach ($queue as $element) {
            echo "$element\n";
        }
    }
}

while (true) {
    echo "\nQueue Operations Menu:\n";
    echo "1. Insert an element\n";
    echo "2. Delete an element\n";
    echo "3. Display queue contents\n";
    echo "4. Exit\n";

    echo "Enter your choice: ";
    $choice = trim(fgets(STDIN));

    switch ($choice) {
        case 1:
            enqueue($queue);
            break;
        case 2:
            dequeue($queue);
            break;
        case 3:
            displayQueue($queue);
            break;
        case 4:
            exit();
        default:
            echo "Invalid choice. Please choose again.\n";
    }
}

?>