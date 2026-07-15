'''
Question 3: Merge Two Dictionaries

Merge two dictionaries into one.

Example:

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

Output:
{'a':1,'b':2,'c':3,'d':4}
'''

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

merge_dic = dict1 | dict2

print(merge_dic)