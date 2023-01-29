import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.25)
    
    snake.move()
    # game_is_on = False
    

screen.exitonclick()