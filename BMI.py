print("Welcome to BMI Calculator")

height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = round(weight/ height ** 2)

if bmi < 18.5:
    print(f"Your Body mas index is {bmi}:  Underweight")
elif bmi < 25:
    print(f"Your Body mas index is {bmi}:  Normal Weight")
elif bmi < 30:
    print(f"Your Body mas index is {bmi}:  Over Weight")
elif bmi< 35:
    print(f"Your Body mas index is {bmi}:  Obese")
else:
    print(f"Your Body mas index is {bmi}: Critically Obese")

