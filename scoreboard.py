from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        # Here the scoreboard is going to the top left side of the screen and then writing the p2 score
        self.display_score()
        # Here the scoreboard is going to the top right side of the screen and then writing the p1 score
        self.display_score()

    def increase_p1_score(self):
        self.p1_score += 1
        self.clear()
        self.display_score()

    def increase_p2_score(self):
        self.p2_score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.goto(100, 220)
        self.write(f"{self.p1_score}", align="center", font=("Courier", 50, "bold"))
        self.goto(-100, 220)
        self.write(f"{self.p2_score}", align="center", font=("Courier", 50, "bold"))

