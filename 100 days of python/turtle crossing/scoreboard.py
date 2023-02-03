from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=-400, y=400)
        self.__update_score()

    def level_up(self):
        self.level += 1
        self.__update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def __update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",
                   align=ALIGNMENT, font=FONT)
