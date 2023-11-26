'''
Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints
1<=len(string)<=200

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string

'''
'''
def count_substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Sample Input
original_string = input().strip()
sub_string = input().strip()

# Sample Output
result = count_substring(original_string, sub_string)
print(result)

'''

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        s=string[i]
        for j in range(i+1, len(string)):
            s+=string[j]
            if len(s)>len(sub_string):
                break
            if s==sub_string:
                count+=1
    return count





