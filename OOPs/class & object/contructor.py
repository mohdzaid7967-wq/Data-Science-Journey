'''
__init__() method is a constructor which is automatically called when a new object of a class is created. Its main purpose is to initialize the object’s attributes and set up its initial state. When an object is created, memory is allocated for it and __init__ helps organize that memory by assigning values to attributes.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("Max", 30)
b = Person("Emilia", 25)

print(a.name, a.age) 
print(b.name, b.age)