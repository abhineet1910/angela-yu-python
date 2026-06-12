#
# import another_module
# print(another_module.abhi)
# from turtle import Turtle, Screen
# tinny = Turtle()
# my_screet = Screen()
# print(my_screet.canvheight)
# print(tinny)
# tinny.shape("turtle")
# tinny.color("DarkOliveGreen")
# tinny.forward(100)
# tinny.left(120)
# tinny.forward(100)
# tinny.left(120)
# tinny.forward(100)
# import prettytable
#
# while True:
#     tinny.forward(200)
#     tinny.left(170)
#     if abs(pos()) < 1:
#         break
# #tinney is the obj and the . is for calling method or atributs
#
#
# my_screet.exitonclick()
# #this give exit of code only when its click o
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("POKEMON NAMES",["pikachu","Pidgeotto","Vivillon"])
table.add_column("TYPE",["electric","flying","flying"])
# table.align["POKEMON NAMES"]="l"
table.align["TYPE"]="l"
table._align["POKEMON NAMES"]="l"
print(table)
