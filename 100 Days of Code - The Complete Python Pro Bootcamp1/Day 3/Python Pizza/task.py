print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    if pepperoni == "Y":
        print("your final bill is $"+15+2)
    else:
        print("your final bill is $"+15)
    if extra_cheese != "Y":
            print("your final bill is $"+15+2)
    else:
            print("your final bill is $"+15+2+1)

elif size == "M":
    if pepperoni == "Y":
        print("your final bill is $"+20+3)
    else:
        if extra_cheese == "Y":
            print("your final bill is $"+20+3+1)
        else:
            print("your final bill is $"+20+3)

elif size == "L":
    if pepperoni == "Y":
        print("your final bill is $"+25+3)
    else:
        if extra_cheese == "Y":
            print("your final bill is $"+25+3+1)
        else:
            print("your final bill is $"+25+3)

else:
    print("your final bill is 0")


