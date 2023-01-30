from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """
    scoreboard
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.__update_score()

    def add_point(self):
        self.score += 1
        self.__update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def __update_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}",
                   align=ALIGNMENT, font=FONT)
