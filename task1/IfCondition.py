# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
BMI = weight / (height ** 2)

if BMI >= 30:
    print("Obesity")
elif 25 <= BMI < 30:
    print("Overweight")
elif 18.5 <= BMI < 25:
    print("Normal")
else:
    print("Underweight")