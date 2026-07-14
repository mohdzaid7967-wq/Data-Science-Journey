'''
Question 5: Remove Duplicate Words

Take a sentence as input and print only unique words using a set.
'''


sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)