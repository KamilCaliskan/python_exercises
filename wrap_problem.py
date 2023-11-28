'''
Input (stdin)

    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    
Output

    ABCD

    EFGH

    IJKL

    IMNO

    QRST

    UVWX

    YZ
'''
def wrap(string, max_width):
    # Use textwrap module to wrap the string
    import textwrap
    wrapped_string = textwrap.fill(string, width=max_width)
    return wrapped_string

if __name__ == '__main__':
    # Sample Input
    input_string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    width = 4

    result = wrap(input_string, width)
    print(result)
