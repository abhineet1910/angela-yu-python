print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 18:
        print("You can ride the rollercoaster")
    elif age >= 16:
        print("You NEED TO PAY 5$")
    else:
        print("You can't ride the rollercoaster")

else:
    print("Sorry you have to grow taller before you can ride.")
