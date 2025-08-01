'''
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
'''

weight = float(input("Enter your weight in kilograms : "))
height = float(input("Enter your high in meters : "))
bmi = weight / height**2
print(f"your bmi = {bmi:.1f}")
if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
elif bmi < 18.5:
    print("underweight")