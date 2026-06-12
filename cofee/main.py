MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resources_sufficent(order_ingrediants):
    for items in order_ingrediants:
        if order_ingrediants[items] > resources[items]:
            print(f"sorry there in not enought {items}")
            return False
    return  True

def process_coins():
    """returns the coins ytou have and you lets """
    print("enter the coins you have ")
    total = int(input("how many quarters do you have "))*0.25
    total += int(input("how many dimes do you have "))*0.1
    total += int(input("how many nickles do you have "))*0.05
    total += int(input("how many pennies do you have "))*0.01
    return total


def is_transaction_sucess(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def resources_left(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


#todo 1 print report statements
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk:{resources['milk']}ml")
       print(f"Coffee:{resources['coffee']} g")
       print(f"Money: {profit}")
    else:
        drint = MENU[choice]
        if is_resources_sufficent(drint["ingredients"]):
            payment = process_coins()
            if is_transaction_sucess(payment,drint['cost']):
                resources_left(choice,drint['ingredients'])
            else:
                is_on = False
        else:is_on = False



