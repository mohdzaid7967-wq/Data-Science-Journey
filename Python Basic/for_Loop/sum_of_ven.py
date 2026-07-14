'''
Question 1: Sum of Even Numbers

Take an integer n as input and print the sum of all even numbers from 1 to n.
'''

number = int(input("Enter the Number: "))

sum = 0

for i in range(number):
    if(i % 2 == 0):
        sum = sum + i
        

print(sum)