

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


if year % 4 == 0:
    print("Leap year")
elif year % 1 != 0:
    print("leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year")
