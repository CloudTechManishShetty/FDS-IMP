import numpy as np

# Function to compute Manhattan distance between two points
def manhattan_distance(point1, point2):
    return np.abs(point1 - point2).sum()

# Function to compute the sum of Manhattan distances between all pairs of points
def sum_of_manhattan_distances(points):
    total_distance = 0
    n = len(points)
    
    # Loop through all pairs of points
    for i in range(n):
        for j in range(i + 1, n):
            total_distance += manhattan_distance(points[i], points[j])
    
    return total_distance

# Example list of points (as numpy arrays)
points = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Calculate the sum of Manhattan distances
total_manhattan_distance = sum_of_manhattan_distances(points)

# Display the result
print("Sum of Manhattan distances between all pairs of points:", total_manhattan_distance)
