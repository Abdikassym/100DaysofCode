from turtle import Turtle
import snake
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.draw_board()

    def draw_board(self):
        self.write(f"Score: {self.points}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, align=ALIGNMENT, font=FONT)

    def eat_food(self):
        self.points += 1
        self.clear()
        self.draw_board()







