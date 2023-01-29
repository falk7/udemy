import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
bet_1 = None
bet_2 = None

while bet_1 not in colors:
    bet_1 = screen.textinput(title="Player 1!", prompt="Who will win the race? Enter a Color!").lower().strip()
while bet_2 not in colors:
    bet_2 = screen.textinput(title="Player 2!", prompt="Who will win the race? Enter a Color!").lower().strip()

starting_ys = [-60, -30, 0, 30, 60, 90]
all_turtles = []

for i in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=starting_ys[i])
    all_turtles.append(new_turtle)

if bet_1 and bet_2:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        steps = random.randint(0,10)
        turtle.forward(steps)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet_1:
                print(f"Player 1 won! The {winning_color} turtle made the win!")
            elif winning_color == bet_2:
                print(f"Player 2 won! The {winning_color} turtle made the win!")
            else:
                print(f"You all lost! The {winning_color} turtle was the first one!")
          
screen.exitonclick() 