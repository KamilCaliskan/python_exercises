import math


AB = int(input())
BC = int(input())

hypotenuse = math.sqrt(AB**2 + BC**2) # Pythagorean Theorem

# Calculate sine of theta
sin_theta = AB / hypotenuse

# Calculate theta in radians
theta_rad = math.asin(sin_theta)

# Convert radians to degrees
theta_deg = theta_rad * (180 / math.pi)

# Round theta to the nearest integer
theta_deg = round(theta_deg)

# Output the result
print(f'{theta_deg}{chr(176)}')
