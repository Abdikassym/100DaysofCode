from turtle import  Screen
import time
from snake import Snake

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("My snake game!")
my_screen.tracer(0)

snake = Snake()

game_is_on = True

my_screen.listen()
while game_is_on:
    my_screen.update()
    time.sleep(0.08)

    snake.move()
    my_screen.onkey(snake.left, "Left")
    my_screen.onkey(snake.right, "Right")
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")








my_screen.exitonclick()
