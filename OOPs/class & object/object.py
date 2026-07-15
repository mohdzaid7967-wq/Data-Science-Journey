'''
Objects
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

State: represented by the attributes and reflects the properties of an object.
Behavior: represented by the methods of an object and reflects the response of an object to other objects.
Identity: gives a unique name to an object and enables one object to interact with other objects.
'''

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)