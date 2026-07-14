'''
Question 2: Remove Duplicates

Remove duplicate elements from a list while keeping the original order.
'''
list = [2,3,4,1,3,5,6,4]

unique_list = []

for num in list:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)