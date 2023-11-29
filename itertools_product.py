'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B)
'''

from itertools import product

# Input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute cartesian product
result = list(product(A, B))

# Output
for item in result:
    print(item, end=' ')
