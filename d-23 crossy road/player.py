from turtle import Turtle
from scoreboard import Score


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(0, -250)

    def step(self):
        self.setheading(90)
        self.fd(10)

    def game_over(self):
        self.goto(10, 180)
        self.write("Game Over.", False, "center", ("Courier", 64, "bold"))

    def next_level(self):
        self.goto(0, -250)

    def step_left(self):
        self.setheading(180)
        self.fd(10)

    def step_back(self):
        self.setheading(270)
        self.fd(10)

    def step_right(self):
        self.setheading(0)
        self.fd(10)

    def next_round(self):
        self.goto(0, -250)
