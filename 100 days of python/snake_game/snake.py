from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self) -> None:
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())

        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction: float) -> None:
        self.head.setheading(direction)

    def up(self):
        if self.head.heading() != DOWN:
            self.set_direction(UP)

    def down(self):
        if self.head.heading() != UP:
            self.set_direction(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.set_direction(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.set_direction(LEFT)
