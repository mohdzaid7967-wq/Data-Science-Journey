'''
Question 2: Sum of Natural Numbers

Take a number n and find the sum of numbers from 1 to n.
'''

num = int(input("Enter the Number: "))

sum = 0

while num >= 1:
    sum = sum + num
    num = num - 1

print(sum)