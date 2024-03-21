def calculate_happiness(array, set_A, set_B):
    happiness = 0
    for num in array:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1
    return happiness

# Reading input
n, m = map(int, input().split())
array = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

# Calculating and printing happiness
result = calculate_happiness(array, set_A, set_B)
print(result)




'''
Sure, let's break down each step:

1. `n, m = map(int, input().split())`: This line reads a line of input from the standard input (keyboard),
splits it into separate strings using the `split()` method (default separator is whitespace), t
hen converts each string to an integer using `map(int, ...)`,
and finally assigns the first integer to `n` and the second integer to `m`. 
This line is used to read the integers `n` and `m` from the input, where `n` represents the number of elements in the array and `m` represents the number of elements in sets A and B.

2. `array = list(map(int, input().split()))`: This line reads another line of input from the standard input, splits it into separate strings, converts each string to an integer, 
and stores the resulting integers in a list named `array`. 
This line reads the elements of the array provided in the input.

3. `set_A = set(map(int, input().split()))`: This line reads another line of input from the standard input,
splits it into separate strings, converts each string to an integer, 
stores the resulting integers in a set named `set_A`. This line reads the elements of set A provided in the input.

4. `set_B = set(map(int, input().split()))`: This line is similar to the previous one. 
It reads another line of input from the standard input, splits it into separate strings, 
converts each string to an integer, and stores the resulting integers in a set named `set_B`. 
This line reads the elements of set B provided in the input.
'''

After executing these four lines, you will have obtained the values of `n`, `m`, `array`, `set_A`, and `set_B` based on the input provided by the user. These values will then be used in further calculations, such as determining the happiness based on the conditions specified in the problem statement.
