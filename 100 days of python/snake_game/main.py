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

game_is_on = True
game_speed = 0.1

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_point()
        snake.extend()
        food.refresh()

    # increase game speed
    #if scoreboard.score != 0 and scoreboard.score % 5 == 0:
    #    game_speed *= 0.9

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            game_speed = 0.1



screen.exitonclick()
