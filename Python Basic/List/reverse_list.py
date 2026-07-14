''''
Question 4: Reverse a List

Reverse a list without using reverse() or slicing ([::-1]).
'''


my_list = [2,3,4,2,5]

reverse_list = []

index = len(my_list) - 1

while index >= 0:
    reverse_list.append(my_list[index])
    index -= 1

print(reverse_list)