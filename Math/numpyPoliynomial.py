import numpy as np

# Read the coefficients of the polynomial and the value of x
coefficients = list(map(float, input().split()))
x = float(input())

# Evaluate the polynomial at the given point
result = np.polyval(coefficients, x)

# Print the result
print(result)
