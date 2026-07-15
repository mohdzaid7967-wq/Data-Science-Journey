from abc import ABC, abstractclassmethod

class Greet(ABC):
    @abstractclassmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
