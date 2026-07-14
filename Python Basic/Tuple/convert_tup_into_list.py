'''
Question 3: Convert Tuple to List

Convert a tuple into a list, add an element, and convert it back to a tuple.
'''

my_tup = (2,4,1,5,6,7)

my_list = list(my_tup)

my_list.append(3)

my_tup = tuple(my_list)

print(my_tup)