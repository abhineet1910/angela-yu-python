# print ("hello eorld")
# abhin_neet = "ABHINEET"
# print(f"here is the bad boy{abhin_neet}comens in ")
# y_sc = 1233
# print(f"{y_sc}is the age of that bitch ")
# sish_c = True
# if sish_c:
#     print("you r true ")
# else:
#     print("you r false")
# name = "abhineet mitra"
# #age = 21
# gpa  = 3.2
# is_student = True
#
# #age = str(age)
# #age += "1"
#
# name = bool(name)
# print(name)
# gpa = int(gpa)
# print(gpa)
# is_student = float(is_student)
# print(is_student)
# #input() = its  a function that used to take input from
# #user and return and save a string if you had to do arthematic u need to type change it
# x =input("enter you name ---")
# age = input("enter you age ---")
# print(f"hey there {x}")
# print(f"your age is {age} ")
# age = int(age)# or you can trake input as integer syntex is like age = int(input("xyz..."))
#
# age = age +1
# print(age)
# #area of the rectangle
# #parameter of the rectangle
# lenght = int(input("enter your lenght ---"))
# breath = int(input("enter your breath ---"))
# y = input("you want area or paramenter ")
# if y == "area":
#     area = lenght * breath
#     print(f"your area is {area}")
# else:
#     yoyo = 2*(lenght+breath)
#     print (f"your perimeter is {yoyo}")
#
#arthematic operations
import math
# item = input("whats item yoou would like to have ")
# price = float(input("whats price of item "))
# quantity= int(input("how much quantity of item you would like to have "))
# total = price * quantity
# print(total)
#basic  maths $arthematics
#dost = 5
#dost = dost +1
# dost += 1 # for addition
# dost -= 2#for substraction
# dost *=3
# dost /= 2
# dost **= 2
# now for the remander part we uses % keyword for that
# remander = dost % 2
# print(remander)
# builtin maths

# c  = 3.14
# y = 4
# z = 50
# # result = round(c)
# result = abs(y)
# # abs is termed as a absulute value of that variable which means distance form zero
# prefer = pow(y, 4)
# print(result)
# print(prefer)
# maxim = max(c,y,z)
# print(maxim)
# #lets build a program to calculate a circumfarrance of acircle
#
# radius = int(input("enter the radius of circcle "))
# y = math.pi
# circumfrence = 2 * y * radius
# print(f"circumference is {round(circumfrence, 2)}")
# #for area of a circle its
# area = math.pi * (radius**2)
# # anathor way is area = a
# print(f" aream is ; {round (area,1)}cm*cm")
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# x = math.sqrt(pow(a,2) + pow(b,2))
# print(x)
#slicing = create a substring by ectracting elements from another string formate [start:stop:step]
# name  = "abhineet mitra"
# first_name = name[0:8]
# print(first_name)
# funky_name = name[0:10:2]
# print(funky_name)
# reversed_name = name[::-1]
# print(reversed_name)
#slicing string
# wesite =  "http://google.com"
# slice = slice(7,-4)
# print(wesite[slice])
# website2 = "http://www.youtube.com"
# print(website2[slice])
# age = int(input("Enter your age: "))
# if age == 18:
#     print("You are old enough to get voter id for  vote")
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are old enough to vote")
# ***logical operator and ,or ,not for and use both the statement must be true
#for or operator either of both of them true then its true
#not is basics used to flip true to falso and false to true
#
#****okay lets build a unit convertor
# numb = float(input("Enter a number: "))
# unit = input("kilogram or pound ? (K or L )")
# if unit == "K":
#     numb = numb * 2.205
#     unit = "lbs"
# elif unit == "L":
#     numb = numb / 2.205
#     unit = "kg"
# else:
#     print(f"{unit} is not a valid unit")
# print(f"your weight is {round(numb, 3)}{unit}")
#****/*letrs create temperature converter
# unit = input("Enter the unit of temperature you would like to convert: Celsius or Fahrenheit ")
# numb = int (input("Enter the temperature : "))
# if unit == "C":
#     numb = (numb * 9/5) + 32
#     unit = (" Celsius")
# elif unit == "F":
#     numb = (numb - 32) *5/9
#     unit = (" Fahrenheit")
# else:
#     print(f"wrong input please check again ")
# print(f"your {round(numb,2)} {unit}")
#**** logical operator
#****or , and , not not is used for the invert the condition (not false , not true )
# temp = int(input("Enter a number: "))
# is_raining = False
# is_sunny = False
# if temp == 35 and temp < 50 or temp < 0   :
#     print (" the out door is cancelet due to cold wheather ")
# elif temp >= 50:
#     print("the out door is cancelet due to too hot ")
# elif temp >= 25 and is_sunny:
#     print("you can go its a sunny day ")
# elif temp <= 16 and not is_sunny:
#     print("you can go its not a sunny day ")
# else:
#     is_raining = True
#     print("you can go out side ")

##****conditional expression = a one line code for if else statement also called a
#*****ternary operator oprint or assign one of two values based on a condition
#******** x if condition else y
# numb = int(input())
# numb2 = int(input("another number "))
# print ("possitive" if numb>0 else "negative")
# print ("even" if numb%2==0 else "odd")
# print(numb if numb > numb2 else numb2)
#****** operations in string
# name = input("enter yiur full name")
# phonenumber = input("enter phone number")
# resilt = len(name)
# resu= name.find("e")
# resu = name.rfind("e")
# rsu = name.capitalize()
# r = name.lower()
# ru = name.upper()
# rs = name.isalpha()
# rv = name.isdigit()
# rep = phonenumber.count("-")
# rd = phonenumber.replace("-"," ")
# rd = rd.replace(" ","")
# print(f"{resu},{rep},{r},{rs},{rsu},{rd},{rv},{rep},{resilt},{ru}")
# username = input("Enter your username: ")
# if len(username) > 12:
#     print("invalid user name user name must not exid 12 digit  ")
#     exit()
# elif username.find(" ") != -1:
#     print("invalid username user name must not contain any space ")
#     exit()
# elif username.isdigit() == False:
#     print("invalid username username must not contain any digit  ")
#     exit()
# else:
#     print("valid username ")
#     exit()
#*string indexing = acessijng elements of a sequence using [] (indexinng operator )
#*****[start : end: stop]
credid_number = "123-4567-8901-23456"
print(credid_number[0])
print(credid_number[0:4])
print(credid_number[5:])
print(credid_number[-5])
print(credid_number[::2])
lastdigit = credid_number[-5::]
print(f"xxx-xxxx-xxxxx-{lastdigit}")
#****formate specifiers == {value:flags} formate a value based on what flags are insted
#while loop = execute some code while some contion remains true

