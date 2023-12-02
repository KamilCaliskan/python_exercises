import re

# Define a function to find start and end indices of overlapping occurrences
def find_start_end_indices(main_string, sub_string):
    # Create a regular expression pattern with positive lookahead to find overlapping occurrences
    pattern = re.compile(f'(?=({re.escape(sub_string)}))')

    # Use finditer to get all matches in the main string
    matches = pattern.finditer(main_string)

    # Iterate through matches and print start and end indices
    for match in matches:
        start_index = match.start(1)
        end_index = match.end(1) - 1  # Adjusting end index since it's inclusive
        print((start_index, end_index))

# Read input strings
main_string = input().strip()
sub_string = input().strip()

# Find and print start and end indices
find_start_end_indices(main_string, sub_string)
