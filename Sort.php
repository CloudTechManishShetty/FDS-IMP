<?php
$array = array("Sagar" => "31", "Vicky" => "41", "Leena" => "39", "Ramesh" => "40");

// a) Ascending order sort by Value
asort($array);
echo "<h2>Ascending Order Sort by Value:</h2>";
foreach ($array as $key => $value) {
    echo "$key => $value<br>";
}

$array = array("Sagar" => "31", "Vicky" => "41", "Leena" => "39", "Ramesh" => "40");


ksort($array);
echo "<h2>Ascending Order Sort by Key:</h2>";
foreach ($array as $key => $value) {
    echo "$key => $value<br>";
}

$array = array("Sagar" => "31", "Vicky" => "41", "Leena" => "39", "Ramesh" => "40");


arsort($array);
echo "<h2>Descending Order Sort by Value:</h2>";
foreach ($array as $key => $value) {
    echo "$key => $value<br>";
}


$array = array("Sagar" => "31", "Vicky" => "41", "Leena" => "39", "Ramesh" => "40");

krsort($array);
echo "<h2>Descending Order Sort by Key:</h2>";
foreach ($array as $key => $value) {
    echo "$key => $value<br>";
}
?>
