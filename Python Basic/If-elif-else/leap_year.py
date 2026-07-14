'''Question 5: Leap Year Checker

Take a year as input.

Rules:

Divisible by 400 → Leap Year
Else if divisible by 100 → Not Leap Year
Else if divisible by 4 → Leap Year
Else → Not Leap Year'''

year = int(input("Enter the year: "))

if(year % 400 == 0 ):
    print(f"It is leap Year {year}")
elif(year % 100 == 0):
    print(f"It is not a leap Year {year}")
elif(year % 4 == 0):
    print(f"It is a Leap Yar {year}")
else:
    print("Enter the correct year")
