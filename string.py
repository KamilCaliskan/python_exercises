'''
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
'''



def mutate_string(s, position, character):
    # Convert the string to a list
    s_list = list(s)
    
    # Modify the character at the given position
    s_list[position] = character
    
    # Join the list back to a string
    modified_string = ''.join(s_list)
    
    return modified_string

# Sample Input
input_string = input()
position, character = map(str, input().split())

# Convert position to an integer
position = int(position)

# Sample Output
result = mutate_string(input_string, position, character)
print(result)
