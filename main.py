import turtle
import pandas as pd
import row

screen = turtle.Screen()
screen.title("US game project ")
image = "blank_states_img.gif"
# this is because turtle only support gif files
screen.addshape(image)
turtle.shape(image)
# to get the cordinates of the screen where we click we have a mathod
# def on_click(x,y):
#     print(x,y)
# turtle.onscreenclick(on_click)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()
states_list = data["state"].to_list()
to_continue = True
# print(states_list)
state_dict ={
    row.state.lower():(row.x,row.y)
    for index,row in data.iterrows()
#     iterrows()= gos through ever rows of the dataframe one by one

}
# there is also another way withouth using row package


# this is the another way to create a dict using csv file and pandas

# states = data["state"].to_list()
# x_cor = data["x"].to_list()
# y_cor = data["y"].to_list()
# states_dict = {}
# for i in range(len(states)):
#     states_dict[states[i].lower()] = (x_cor[i],y_cor[i])
# print(states_dict)

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 stater correct", prompt="Whats another State")
    answer = answer.lower()
    if answer =="quit":
        missing_state = []
        for state in states_list:
            if state not in guessed_states:
                missing_state.append(state)
        newdata = pd.DataFrame(missing_state)
        newdata.to_csv("states_to_learn.csv")




        break
    if answer in state_dict:
        guessed_states.append(answer)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        cordinate = state_dict[answer]
        writer.goto(cordinate)
        writer.write(answer.title())






