from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


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
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__update_score()

    def add_point(self):
        self.score += 1
        self.__update_score()

    def get_highscore(self):
        with open("hs.txt", encoding="UTF-8") as file:
            return int(file.read())

    def save_highscore(self, score):
        self.high_score = score
        with open("hs.txt", mode="w", encoding="UTF-8") as file:
            file.write(f"{score}")
    
    def reset(self):
        if self.score > self.high_score:
            self.save_highscore(self.score)
        self.score = 0
        self.__update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def __update_score(self):
        self.clear()
        self.goto(x=0, y=230)
        self.write(f"Score: {self.score}, High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)
