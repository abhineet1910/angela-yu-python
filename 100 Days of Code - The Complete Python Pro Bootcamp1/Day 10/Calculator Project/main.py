def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operators["*"](5,8))

def calculate():
    import art
    print(art.logo)
    n1 = float(input("enter the first number"))
    setcontinue = True
    while setcontinue :
        for symbol in operators:
            print(symbol)
        operat = input("enter the operatoion symbball")
        n2 =float(input("enter the second number"))
        answer = operators[f"{operat}"](float(n1), float(n2))
        print(f"{n1}{operat}{n2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            setcontinue = False
            print("\n" * 20)
            calculate()
calculate()








