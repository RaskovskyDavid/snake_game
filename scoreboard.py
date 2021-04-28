from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.update_scroeboard()

    def update_scroeboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: ´{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scroeboard()

    def increase_score(self):
        self.score += 1
        self.update_scroeboard()


