from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color("coral")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_cord = randrange(-380, 380, 20)
        y_cord = randrange(-280, 280, 20)
        self.goto(x_cord, y_cord)

