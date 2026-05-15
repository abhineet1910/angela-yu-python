# import csv
# #
# # data = []
# # temperature = []
# # with open("weather_data1.csv") as csvfile:
# #     reader = csv.reader(csvfile)
# #     next(reader)
# #     # one more way to this instead of using nextr
# #
# #     for row in reader:
# #         print(row)
# #         print(row[1])
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #         temp = int(row[1])  # index 1 = temp column
# #         temperature.append(temp)
# #     print(temperature)
#
# import pandas
# # data = pandas.read_csv("weather_data1.csv")
# # print(data)
# # tem = data["temp"].tolist()
# # print(tem)
# # averge = data["temp"].mean()
# # print(averge)
# # print(data["temp"].max())
# # print(data.condition)
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_f = monday_temp*9/5 + 32
# # print(monday_temp)
# # print(monday_temp_f)
# # creating dat aframe from scratch
# # lets have a dict
# data_dict = {"student":["abhineet","prachi","kamya"],"score":[10,8,6]
# }
# dot = pandas.DataFrame(data_dict)
# print(dot)
# dot.to_csv("new_data.csv",index=False)
#
# data = pandas.read_csv("new_data.csv")
# print(data)
# print(data["score"])
# print(data[data.score==data.score.max()])
import pandas
import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data["Primary Fur Color"])
count_gray =(data['Primary Fur Color'] == 'Gray').sum()
count_red = (data['Primary Fur Color'] == 'Cinnamon').sum()
count_black =(data['Primary Fur Color'] == 'Black').sum()
# one more way to do that ia
gray = len(data[data['Primary Fur Color'] == 'Gray'])
print(gray)
# print(count_gray)
# print(count_red)
# print(count_black)
colour_data = {
    "Fur colour":("Gray","Cinnamon","Black"),
    "count":(count_gray,count_red,count_black)
}
data = pandas.DataFrame(colour_data)
# print(data)
data.to_csv('squiral_colour.csv',index=False)
colour = pd.read_csv("squiral_colour.csv")
print(colour)