'''
Question 2: Largest of Three Numbers

Create a function that accepts three numbers and returns the largest.

Example:

Input:
10, 25, 15

Output:
25
'''

def largest_num(a,b,c):
    if a > b and a > c:
        return f"a is the largest number among three{a} "
    elif b > a and b > c:
        return f"b is the largest number among three {b}"
    else:
        return f"c is the largest number among three {c}"
    
result = largest_num(21,3,5)
result_1 = largest_num(23,44,5)
result_2 = largest_num(2,3,16)

print(result)
print(result_1)
print(result_2)