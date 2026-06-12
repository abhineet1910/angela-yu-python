for number in range(1,101):
    no = number
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 15 == 0:
        print("fizzbuzz")
    else:
        print(number)