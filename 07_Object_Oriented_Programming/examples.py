# Defining a Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an Object
person = Person("Alice", 30)
print(person.greet())

# Inheritance Example
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student("Bob", 20, "S123")
print(student.greet())