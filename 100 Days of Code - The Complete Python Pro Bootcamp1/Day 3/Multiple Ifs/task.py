print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if 5>age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wantspohoto = input("Would you like to see the photo? (y/n)")
    if wantspohoto == "y":
        print("Here is your photo hyou need extra 3 $:")
        bill += 3

    print(f"Here is your final bill {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

