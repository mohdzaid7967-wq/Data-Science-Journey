'''
Question 3: Second Largest Number

Find the second largest number in a list.

Example:

Input: [10, 20, 5, 40, 30]
Output: 30
'''


list = [10,20,30,40]

largest = second_largest = float('-inf')

for num in list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)