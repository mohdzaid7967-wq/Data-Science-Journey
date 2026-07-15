class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.__salary = salary
    
emp1 = Employee("Zaid",15000)
print(emp1.name)
print(emp1.__salary) # it will give you error, You can not access private attribute outsie the class

