'''
3. Private members
Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data. In Python, private members are defined with a double underscore prefix (e.g., self.__salary).

Python uses name mangling, where the interpreter internally renames the variable (for eg, __salary becomes _ClassName__salary). This discourages direct access from outside the class, although it does not create strict privacy like other languages.


'''


class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.__salary = salary
    
    def show(self):
        print("Salary", self.__salary)



emp1 = Employee("Zaid",15000)

print(emp1.name)
emp1.show()
print(emp1.__salary) # it will give you error, You can not access private attribute outsie the class