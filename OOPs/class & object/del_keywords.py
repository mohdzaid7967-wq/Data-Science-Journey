class Strudent:
    def __init__(self,name):
        self.name = name 
    
s1 = Strudent("Zaid")
print(s1.name)

# delete property
del s1.name
print(s1.name)