'''
Question 4: Find Key by Value

Given a value, print its corresponding key.

Example:

{
'A':10,
'B':20,
'C':30
}

Input:
20

Output:
B
'''

my_dic = {
    'A' : 10,
    'B' : 20,
    'C' : 30 
}

target = int(input("Enter the value: "))

for key, value in my_dic.items():
    if value == target:
        print(key)
        break