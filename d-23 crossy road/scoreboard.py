import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(-235, 275)
        self.level = 0
        self.draw_score()

    def add_score(self):
        self.clear()
        self.level += 1
        self.draw_score()

    def draw_score(self):
        self.write(f"Score: {self.level}", False, "center", ("Courier", 16, "bold"))
