# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
def greet(name="name",age="age",gender="gender"):
    if gender == "male":
         print(f"Hello mr {name}, you are {age} years old.")
    else:
        print(f"Hello miss {name}, you are {age} years old.")

greet("Jack Bauer",22,"male")