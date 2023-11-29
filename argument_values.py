'''
Python supports a useful concept of default argument values
For each keyword argument of a function
we can assign a default value which is going to be used as the value of said argument 
if the function is called without it
For example, consider the following increment function:

def increment_by(n, increment=1):
    return n + increment

The functions works like this:

>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>
'''
class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        self.current += 2
        return self.current - 2


class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        self.current += 2
        return self.current - 2


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


# Sample Input
queries = int(input().strip())
for _ in range(queries):
    stream_name, n = input().strip().split()
    n = int(n)
    
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
