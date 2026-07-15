'''
. Protected members
Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).
'''

class Employee:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    

class SubEmployee(Employee):
    def show(self):
        print("Age", self._age) # access in subclass (derived class )


emp1 = SubEmployee("Zaid", 22)
print(emp1.name)
emp1.show()