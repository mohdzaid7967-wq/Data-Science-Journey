'''
Question 2: Largest Number

Use a lambda function to find the larger of two numbers.

Example:

Input:
10, 25

Output:
25
'''

largest_num = lambda a,b: a if a > b else b

num1 = int(input("Enter the fisrt number: "))
num2 = int(input("Enter the second number: "))

result = largest_num(num1,num2)

print(result)