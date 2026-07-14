'''
Question 4: Reverse a Number

Take an integer and print its reverse.

Example

Input:
12345

Output:
54321
'''

num = int(input("Enter the Number: "))
reverse_num = 0

while num > 0:
    digit = num % 10 
    reverse_num = (reverse_num * 10 ) + digit
    num = num // 10 

print(reverse_num)