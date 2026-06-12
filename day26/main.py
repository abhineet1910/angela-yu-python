# student_dict = {
#     "names":["abhineet","prachi","kamya","preet"],
#     "rating":[10,7,9,5]
#
# }
# for [key ,value] in student_dict.items():
#     print(key)
#     # print(value)
# import pandas as pd
# df = pd.DataFrame(student_dict)
# # print(df)
# for (key,value) in df.items():
#     print(value)
#     # print(value)
# for (index,row) in df.iterrows():
#     # print(row.rating)
#     # print(row.name)
#     if row.name == "kamya":
#         print(row.rating)
import csv

with open("nato_phonetic_alphabet.csv", "r") as f:
    print(f.read())
name_dict = {row.letter,new_v for(index,row) in f.iterrows()}