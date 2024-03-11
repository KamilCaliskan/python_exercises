'''
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of
members per group where K≠1

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. The room numbers will appear

times per group except for the Captain's room

Mr. Anant needs you to help him find the Captain's room number
The total number of tourists or the total number of groups of families is not known to you
You only know the value of
K and the room number list
'''
# Read input
group_size = int(input())
room_numbers = list(map(int, input().split()))

# Initialize a dictionary to count occurrences of room numbers
room_count = {}

# Count occurrences of each room number
for room_number in room_numbers:
    room_count[room_number] = room_count.get(room_number, 0) + 1

# Find the room number that occurs only once (Captain's room)
for room_number, count in room_count.items():
    if count == 1:
        captains_room = room_number
        break

# Print the Captain's room number
print(captains_room)
