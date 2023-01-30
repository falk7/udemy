from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        rand_loc = self._create_random_location()
        self.goto(rand_loc)

    def refresh(self):
        """
        goes to new random location
        """
        rand_loc = self._create_random_location()
        self.goto(rand_loc)

    def _create_random_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        return (x, y)
