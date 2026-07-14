'''
Question 3: Count Vowels

Take a string as input and count how many vowels (a, e, i, o, u) are present using a for loop.
'''

str = input("Enter the String : ")

vowels = ['a','e','i','o','u','A','E','I','O','U']

count = 0

for i in str:
    if i in vowels:
        count += 1


print(count)