# Importing a Built-in Module
import math
print("Square root of 16:", math.sqrt(16))

# Creating and Using a Custom Module
# Save this as my_module.py in the same directory
def greet(name):
    return f"Hello, {name}!"

# Importing the Custom Module
import my_module
print(my_module.greet("TechSpark"))