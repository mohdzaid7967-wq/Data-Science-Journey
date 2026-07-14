'''Question 2: BMI Calculator

Take two inputs:

Weight (kg)
Height (meters)'''

weight = float(input("Enter the weight: "))
height = float(input("Enter your Height in CM: "))

height = height / 100

BMI = weight / (height ** 2)

print("You BMI is: ", round(BMI, 2))

if(BMI < 18.5):
    print("You are underwight")
elif(18.5 < BMI < 24.9):
    print("You are Normal")
elif(25 < BMI < 29.9):
    print("You are OverWeight")
elif(BMI >= 30):
    print("You are Obese")
else:
    print("Enter Your correct weight and height")
