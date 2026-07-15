'''
Question 3: Factorial

Write a function to calculate the factorial of a number.

Example:

Input:
5

Output:
120
'''

def factorial(num):
    ans = 1

    while num > 0: 
        ans = num * ans
        num = num - 1

    return ans


result = factorial(5)

print(result)