'''
Question 2: Word Frequency

Count the frequency of each character in a string using a dictionary.

Example:

Input:
hello

Output:
{
'h':1,
'e':1,
'l':2,
'o':1
}
'''

str = input("Enter the string: ")

word_frequency = {}

for char in str:
    if char in word_frequency:
        word_frequency[char] += 1
    else:
        word_frequency[char] = 1

print(word_frequency)