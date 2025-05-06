# Decorator Example
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

# Generator Example
def generate_numbers():
    for i in range(5):
        yield i

for number in generate_numbers():
    print(number)