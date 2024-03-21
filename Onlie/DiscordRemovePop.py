n = int(input())  # Number of elements in the set
s = set(map(int, input().split()))  # Create the set with given elements

num_commands = int(input())  # Number of commands to execute

# Execute the commands
for _ in range(num_commands):
    command = input().split()  # Split the command and value
    if command[0] == 'pop':
        s.pop()  # Remove and return an arbitrary element
    elif command[0] == 'remove':
        s.remove(int(command[1]))  # Remove the specified element
    elif command[0] == 'discard':
        s.discard(int(command[1]))  # Remove the specified element if it exists, otherwise do nothing

# Output the sum of elements in the set
print(sum(s))
