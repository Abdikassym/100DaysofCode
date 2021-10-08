from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.speed(1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
