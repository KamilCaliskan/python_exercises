
def split_and_join(line):
    # Split the input string on a space delimiter
    words = line.split(" ")

    # Join the words using a hyphen
    result = "-".join(words)

    return result

# Sample Input
input_string = "this is a string"

# Sample Output
output_string = split_and_join(input_string)
print(output_string)
