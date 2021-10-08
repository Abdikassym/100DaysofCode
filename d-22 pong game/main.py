import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball((0, 0))
r_score = Scoreboard((300, 250))
l_score = Scoreboard((-300, 250))

speed = 0.1

game_is_on = True

screen.listen()
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    if ball.xcor() >= 350 and ball.distance(r_paddle) < 60 or ball.xcor() <= -360 and ball.distance(l_paddle) < 60:
        ball.collision()

    if ball.xcor() > 390:
        l_score.draw()
        ball.reset_position()
        ball.ball_speed = 0.1

    elif ball.xcor() < -390:
        r_score.draw()
        ball.reset_position()
        ball.ball_speed = 0.1

# 5 detect collision with wall and bounce
# 6 detect collision with paddle
# 7 detect when paddle misses
# 8 keep score








screen.exitonclick()
