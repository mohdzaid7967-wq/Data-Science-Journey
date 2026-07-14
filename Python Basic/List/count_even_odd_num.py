''''
Question 5: Count Even and Odd Numbers

Count how many even and odd numbers are present in a list.
'''


my_list = [2,3,5,4,6,7,8,1,10]

sum_even = 0
sum_odd = 0

for num in my_list:
    if num % 2 == 0:
        sum_even += 1
    elif num % 2 != 0:
        sum_odd += 1
    

print(f"Sum of Even number in list {sum_even}")
print(f"Sum of Odd number in list {sum_odd}")