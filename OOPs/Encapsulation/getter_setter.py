'''
Getter and Setter Methods
In Python, getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:

Read data using a getter method.
Update data using a setter method with optional validation or restrictions.
Example: This example shows how to use a getter and a setter method to safely access and update a private attribute (__salary).
'''

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid Salary amount")

emp1 = Employee(5000)

print(emp1.get_salary())  # Access salary using getter

emp1.set_salary(6000)
print(emp1.get_salary()) # Update salary using setter

'''
Explanation:

__salary is a private attribute, so it can't be accessed directly from outside the class.
get_salary() is a getter method that safely returns the current salary.
set_salary(amount) is a setter method that updates the salary only if the amount is positive.
The object emp uses these methods to access and modify the salary while keeping the data protected.
'''