from functools import wraps

def make_blink(function):
    """ Define Decorator """
    @wraps(function)

    def decorator():
        ret = function()

        return "<blink>" + ret + "</blink>"

    return decorator
    
def hello_world():
    return "Hello World"

print(hello_world())

# Verify if the function
print(hello_world.__name__)

# Verify if the docstring remains the same
# print(hello_world.__doc__)