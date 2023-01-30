import time

from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_point()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    # game_is_on = False


screen.exitonclick()
