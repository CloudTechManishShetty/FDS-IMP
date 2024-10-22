<?php

// Array of 15 high temperatures for a spring month
$highTemperatures = [
    58, 62, 68, 72, 75, 78, 80, 82, 85, 80, 75, 70, 65, 60, 58
];

// Calculate average high temperature
$averageHighTemp = array_sum($highTemperatures) / count($highTemperatures);

// Find the five warmest high temperatures
arsort($highTemperatures);
$warmestHighTemps = array_slice($highTemperatures, 0, 5);

?>

<!DOCTYPE html>
<html>
<head>
    <title>Spring Month High Temperatures</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Spring Month High Temperatures</h1>
    
    <h2>Average High Temperature: <?= number_format($averageHighTemp, 2) ?>°F</h2>
    
    <h2>Five Warmest High Temperatures:</h2>
    <table>
        <tr>
            <th>Rank</th>
            <th>Temperature (°F)</th>
        </tr>
        <?php foreach ($warmestHighTemps as $rank => $temp) { ?>
        <tr>
            <td><?= $rank + 1 ?></td>
            <td><?= $temp ?></td>
        </tr>
        <?php } ?>
    </table>
</body>
</html>