''''
Question 2: Find Maximum Value

Find the maximum element in a tuple without using max().
'''

my_tup = (2,4,2,4,5,6,8)

largest = my_tup[0]

for num in my_tup:
    if num > largest:
        largest = num

print(largest)
print(my_tup)