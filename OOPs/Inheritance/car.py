class Car:
    @staticmethod
    def start():
        print("Car Started..!")

    @staticmethod
    def stop():
        print("Car Stoped...!")
    

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name 


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Perus")

print(car1.name)
print(car1.start())
print(car1.stop())

print(car2.name)
print(car2.start())
print(car2.stop())