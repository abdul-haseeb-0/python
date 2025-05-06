# Reading a File
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, TechSpark!")

# Appending to a File
with open("example.txt", "a") as file:
    file.write("\nWelcome to Python!")