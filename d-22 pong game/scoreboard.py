from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.score = -1
        self.draw()

    def draw(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, align="center", font=("Courier", 24, "normal"))
