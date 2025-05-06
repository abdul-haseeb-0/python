# Defining a Function
def greet(name):
    return f"Hello, {name}!"

# Calling the Function
print(greet("TechSpark"))

# Lambda Function
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Function with Default Argument
def add(a, b=10):
    return a + b

print("Addition:", add(5))