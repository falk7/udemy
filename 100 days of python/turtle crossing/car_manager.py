from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.ys = [y*60 for y in range(-7, 8) if y % 2 == 0]
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_car()

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def spawn_car(self):
        car = Turtle(shape="square")
        car.shapesize(stretch_len=6, stretch_wid=3)
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(x=580, y=choice(self.ys))
        self.cars.append(car)

    def manage_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

            if car.xcor() < -640:
                self.cars.remove(car)
                car.clear()
                car.hideturtle()

        if randint(1, 6) == 1:
            print(len(self.cars))
            self.spawn_car()

    def detect_collision(self, player: Turtle) -> bool:
        for car in self.cars:
            if player.distance(car) < 45:
                return True