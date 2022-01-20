height = int(input("What is your height? "))


if height >= 120:
    print("You can ride!!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you must grow taller before you can ride")


# var below are for different exercise,
#  Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#  Don't change the code above


# Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print("Your BMI is {bmi}, you are obese.")
else:
    print("Your BMI is 40, you are clinically obese.")

#print(f"Your BMI is {bmi}. You are slightly over weight")
