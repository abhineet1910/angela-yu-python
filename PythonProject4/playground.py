def add(*args):
    total = 0
    for arg in args:
        total += arg

    print(sum(args))
    print(args[1])
    return total
print(add(6,7,8,9))

def calc(num, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    if "add" in kwargs:
        num += kwargs["add"]

    if "multiply" in kwargs:
        num *= kwargs["multiply"]
    print(num)
calc(25,multiply=5)
class car:
    def __init__(self,**kw):
        self.name = kw.get("name")
        self.price = kw.get("price")
my_car = car(name = "gtr")
print(my_car.name)
print(my_car.price)


