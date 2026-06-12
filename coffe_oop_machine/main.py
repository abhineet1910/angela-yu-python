from random import choice

import menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu,MenuItem
money_machine = MoneyMachine()
money_machine.report()
cofee_maker = CoffeeMaker()
cofee_maker.report()


my_menu=Menu()
is_on = True
while is_on:
    option =my_menu.get_items()
    choice = input(f"what would you like to have ?{option}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        # print(drink)
        resources = cofee_maker.is_resource_sufficient(drink)
        if resources:
            if resources and money_machine.make_payment(drink.cost):
                cofee_maker.make_coffee(drink)





# get_items=get_items()
# my_menu=Menu()
# my_menu.__init__()
# menu_item = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
# menu_item.__init__(name="latte", water=200, milk=150, coffee=24, cost=2.5)
# menu_item.__init__(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
# menu_item.__init__(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
# # my_first = my_menu.
