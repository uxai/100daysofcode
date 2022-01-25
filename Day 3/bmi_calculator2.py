height = float(input("Enter your height in m: ")) 
weight = float(input("Enter your weight in kg: "))

bmi = round((weight / (height ** 2)), 1)

if bmi <= 18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi} and you are normal weight")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi} and you are overweight")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")