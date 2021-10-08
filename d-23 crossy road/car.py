from turtle import Turtle
from random import randint, choice, randrange

colors = ["red", "orange", "blue", "green", "brown", "purple", "black", "pink", "yellow", "aquamarine", "coral"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.speed(0)
        self.penup()
        self.goto(randint(300, 700), randrange(-200, 200, 30))
        self.move_speed = randint(5, 15)
        self.setheading(180)

    def move(self):
        self.goto(self.xcor() - self.move_speed, self.ycor())
        self.restart()

    def restart(self):
        if self.xcor() < -300:
            self.goto(randint(300, 550), randrange(-200, 200, 30))
