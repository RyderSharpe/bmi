# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.
#
# BMI = Weight/Height^2
#
# Example Input 1
# 1.50
# 63
# Example Output 1
# Your BMI is 28.0, you are slightly overweight.

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg? "))

bmi = weight / height**2
print(f"Your BMI is: {bmi}")

if bmi <= 18.5:
    print("You are underweight")
elif 18.5 < bmi < 25:
    print("Your weight is normal")
elif 25 <= bmi < 30:
    print("You are slightly overweight")
elif 30 <= bmi < 35:
    print("You are obese")
elif 35 <= bmi:
    print("Very Obese")

else:
    print("You are overweight")




