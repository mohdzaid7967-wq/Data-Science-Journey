'''
Declaring Protected and Private Methods
In Python, you can control method access levels using naming conventions:

Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
Use a double underscore (__) to define a private method accessible only within class due to name mangling.
Note: Unlike other programming languages, Python does not enforce access modifiers like public, private or protected at the language level. However, it follows naming conventions and uses a technique called name mangling to support encapsulation.

Example: This example demonstrates how a protected method (_show_balance) and a private method (__update_balance) are used to control access. The private method updates balance internally, while protected method displays it. Both are accessed via a public method (deposit), showing how Python uses naming conventions for encapsulation.
'''

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def _show_balanc(self):
        print(f"Balance: {self.balance}") # Protected method
    
    def __update_balance(self,amount): # private method
        self.balance += amount
    
    def deposit(self,amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balanc()
        else:
            print("Invalid deposit amount!")


account1 = BankAccount(10000)
account1._show_balanc()
print("After deposit amount!")
account1.deposit(500)

# account.__update_balance(500)  # Error: private method