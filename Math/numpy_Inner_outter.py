import numpy as np

# Read the input arrays
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

# Compute the inner product
inner_product = np.inner(A, B)

# Compute the outer product
outer_product = np.outer(A, B)

# Print the inner product
print(inner_product)

# Print the outer product
print(outer_product)
