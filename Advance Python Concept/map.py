number = [1,2,3,4,5]

def square(x):
    return x * x

new = list(map(square,number))

print(new)