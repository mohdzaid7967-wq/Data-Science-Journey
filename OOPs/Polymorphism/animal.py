class Animal:
    def sound(self):
        print("Make some genric sound")
    
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meo"
    

animals = [Dog(),Cat(),Animal()]

for animal in animals:
    print(animal.sound())