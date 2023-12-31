str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
---------------------
The any() function in Python is commonly used when you want to check if at least one element in an iterable evaluates to True. It returns True if at least one element is True, and False otherwise. This can be useful in various scenarios where you have a collection of values and you want to determine if any of them meet a certain condition.

Here are a few examples of scenarios where any() can be useful:

    Checking if Any Element in a List Meets a Condition:

    python

numbers = [1, 3, 5, 7, 9, 10]
is_even = any(num % 2 == 0 for num in numbers)
print(is_even)  # True, because 10 is even

Validating User Input:

python

user_input = input("Enter a password: ")
is_valid = any(char.isnumeric() for char in user_input)
print(is_valid)  # True if the password contains at least one numeric character

---------------------
The if __name__ == '__main__': block in Python is used to check whether the Python script is being run as the main program or if it is being imported as a module into another script. Here's what each part of the statement means:

    __name__: It is a special built-in variable in Python. When a Python script is executed, __name__ is set to '__main__' if the script is the main program being run. If the script is being imported as a module into another script, __name__ is set to the name of the script/module.

    ==: This is the equality operator, which checks if the left side is equal to the right side.

    '__main__': This is a string literal representing the name of the main program.

The entire statement if __name__ == '__main__': checks whether the Python script is being run as the main program. If it is the main program, the code inside the block will be executed. If the script is being imported as a module, the code inside the block will not be executed.

In the given context:

python

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

This ensures that the code inside the block is only executed when the script is run as the main program. The n = int(input()) line takes user input for the variable n, and then the print_formatted(n) function is called with the user-provided input. This structure allows you to use the script both as a standalone program and as a reusable module that can be imported into other scripts without executing the main code block.
