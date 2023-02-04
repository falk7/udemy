from turtle import Turtle, Screen
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

screen = Screen()
screen.title("us states game")
screen.setup(height=491, width=725)
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic("blank_states_img.gif")

csv = pandas.read_csv("50_states.csv")
states = csv["state"].to_list()

names = Turtle()
names.hideturtle()
names.penup()

game_is_on = True
correct_answers = []
while game_is_on:
    answer = screen.textinput(title=f"{len(correct_answers)}/{len(states)} correct states", prompt="Guess a state of the US")
    for index, state in enumerate(states):
        if answer == "Exit" or answer == None:
            game_is_on = False 
            pandas.DataFrame([a for a in states if a not in correct_answers]).to_csv("learnthose.csv")
        if answer.title() == state:
            row = csv[csv.state == state]
            x = int(row.x)
            y = int(row.y)

            names.goto(x,y)
            names.write(state,font=FONT,align=ALIGNMENT)
            correct_answers.append(states.pop(index))

