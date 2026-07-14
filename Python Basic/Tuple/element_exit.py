'''
Question 4: Check Element Exists

Check whether a given element exists in a tuple.
'''

my_tup = (10,20,30,40,50)

find_ele = int(input("Enter the number: "))

for num in my_tup:
    if num == find_ele:
        print(f"The number exist in tuple {find_ele}")
    else:
        print(f"The number is not exist in tuple {find_ele}")
    break