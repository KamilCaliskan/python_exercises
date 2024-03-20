import numpy as np

# Read the dimension of the square matrix
n = int(input())

# Read the elements of the square matrix
matrix = []
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert the list of lists into a NumPy array
matrix = np.array(matrix)

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

# Print the determinant rounded to 2 decimal places
print(round(determinant, 2))
