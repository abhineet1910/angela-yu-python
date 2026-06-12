
with open("/Users/abhin/Documents/my_file.txt", "r") as file:
    content = file.read()
    print(content)
with open("../../Documents/my_file.txt") as data:
    print(data.read())
# with open("new_file.txt",mode= "a") as file:
#     file.write("\nokay well thought keep the consistensy")
