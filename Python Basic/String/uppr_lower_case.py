'''
Question 2: Count Uppercase and Lowercase

Take a string and count:

Uppercase letters
Lowercase letters

Example

Input:
PyThOn

Output:
Uppercase: 3
Lowercase: 3
'''

str = input("Enter the String: ")

uppar_count = 0
lower_count = 0

for char in str:
    if char.isupper():
        uppar_count += 1
    elif char.islower():
        lower_count += 1

print("Uppar Count", uppar_count)
print("Lower Count", lower_count)