'''Question 3: Electricity Bill

Calculate the electricity bill based on these rules:

Units	Price
0–100	₹5/unit
101–300	₹7/unit
Above 300	₹10/unit'''


unit = int(input("Enter the unit: "))

if(0 < unit < 100):
    bill = unit * 5
    print(f"The amount of bill is {bill}")
elif(101 < unit < 300):
    bill = unit * 7
    print(f"The amount of bill is {bill}")
elif(unit > 300):
    bill = unit * 10 
    print(f"The amount of bill is {bill}")
