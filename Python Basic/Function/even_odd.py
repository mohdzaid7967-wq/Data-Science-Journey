'''
Question 1: Even or Odd

Write a function that takes a number as input and returns whether it is Even or Odd.
'''

def even_odd(number):
    if number % 2 == 0:
        return "It is even"
    elif number % 2 != 0:
        return "It is Odd"

number = int(input("Enter the number: "))

result = even_odd(number)
print(result)