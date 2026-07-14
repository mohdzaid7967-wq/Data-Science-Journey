'''
Question 1: Find the Largest Number

Write a program to find the largest number in a list without using max().
'''

list = [22,44,54,63,81,93,0,1,3,5,6,77,8,10]

largest = list[0]

for num in list:
    if num > largest:
        largest = num 

print(largest)

