'''
Question 5: Employee Salary Update

Store employee names and salaries in a dictionary. Increase each salary by 10% and print the updated dictionary.

Example:

Input:
{
'Amit':30000,
'Neha':40000
}

Output:
{
'Amit':33000,
'Neha':44000
}
'''

employe = {
    "Zaid" : 25000,
    "Hammad" : 21000,
    "Amaan" : 17000,
    "Abdullah" : 24000
}

for name in employe:
    employe[name] = int(employe[name] * 1.10)

print(employe)