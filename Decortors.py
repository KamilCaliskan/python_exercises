'''
The Python language provides a simple yet powerful syntax called ‘decorators’
A decorator is a function or a class that wraps (or decorates) a function or a method
The ‘decorated’ function or method will replace the original ‘undecorated’ function or method
Because functions are first-class objects in Python, this can be done ‘manually’, 
but using the @decorator syntax is clearer and thus preferred
'''
def foo():
    # do something

def decorator(func):
    # manipulate func
    return func

foo = decorator(foo)  # Manually decorate

@decorator
def bar():
    # Do something
# bar() is decorated
