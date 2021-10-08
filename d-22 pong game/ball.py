from paddle import Paddle


class Ball(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.shape("circle")
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.bounce()

    def bounce(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1

    def collision(self):
        self.x_move *= -1
        self.ball_speed -= 0.005
        if self.ball_speed == 0:
            self.ball_speed = 0.005

