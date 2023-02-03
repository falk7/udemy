import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=1200)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.manage_cars()

    # detect collision
    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

    # check finish line
    if player.finished():
        scoreboard.level_up()
        car_manager.increase_car_speed()
        player.reset_position()


screen.exitonclick()