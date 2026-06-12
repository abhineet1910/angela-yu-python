
inp = "yes"

while inp == "yes":
    year = int(input("What's your year of birth?"))
    if year > 1980 and year <= 1994:
        print("You are a millennial.")
    elif year > 1994:
        print("You are a Gen Z.")
    else:
        print("your input doesnt count in millenial od genz")

    inp = input("Continue? ")