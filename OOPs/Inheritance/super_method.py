'''
super() Function
super() function is used to call methods from a superclass following Python’s Method Resolution Order (MRO). In particular, it is commonly used in the child class's __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.
'''

class Animal:
    def __init__(self,name):
        self.name = name 
    
    def info(self):
        print("Animal name: ",self.name)

class Dog(Animal):
    def __init__(self,name, breed):
        # Calls constructor based on MRO
        super().__init__(name)
        self.breed = breed
    
    def details(self):
        print(self.name, "is a ", self.breed)
    
d = Dog("Buddy","Golden Retriever")
d.info()
d.details()