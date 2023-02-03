from turtle import Turtle

STARTING_POSITION = (0, -550)
MOVE_DISTANCE = 60
FINISH_LINE_Y = 560


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.color("black")
        self.reset_position()
        self.setheading(90)
        self.shapesize(stretch_len=2,stretch_wid=2)

    def finished(self):
        return self.ycor() > FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
