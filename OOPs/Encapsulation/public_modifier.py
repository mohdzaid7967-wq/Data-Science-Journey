'''
1. Public Members
Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).
'''

class Employee:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def display_info(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    

emp1 = Employee("Zaid",22)

emp1.display_info()
print(emp1.age)
print(emp1.name)