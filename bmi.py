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

#maybe redundant?
bmi = round(weight / height**2, 1)
print(f"Your BMI is {bmi:.1f}, ", end="")

#if bmi <= 18.5:
    #print(f"your bmi is {bmi}, you are underweight")

if bmi <= 18.5:
    print("you are underweight.")
elif 18.5 < bmi < 25:
    print("you have a normal weight.")
elif 25 <= bmi < 30:
    print("you are slightly overweight.")
elif 30 <= bmi < 35:
    print("you are obese.")
elif 35 <= bmi:
    print("you are clinically obese.")
else:
    print("You are overweight")
