'''
If we want to add a single element to an existing set, 
we can use the .add() operation
It adds the element to the set and returns 'None'
'''



n = int(input())  # Total number of country stamps
country_stamps = set()  # Initialize an empty set to store country stamps

# Iterate through the country stamps and add them to the set
for _ in range(n):
    stamp = input()  # Read the country stamp
    country_stamps.add(stamp)  # Add the stamp to the set

# Output the total number of distinct country stamps
print(len(country_stamps))
