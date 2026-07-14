'''
Question 2: Multiplication Table

Take a number as input and print its multiplication table up to 10.
'''

num = int(input("Enter the table Number: "))

for i in range(1,11):
    table = num * i 
    print(num,"*",i,"=" , table)