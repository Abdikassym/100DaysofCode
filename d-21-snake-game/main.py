from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("My snake game!")
my_screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

game_is_on = True

my_screen.listen()
while game_is_on:
    my_screen.update()
    time.sleep(0.065)

    snake.move()
    my_screen.onkey(snake.left, "Left")
    my_screen.onkey(snake.right, "Right")
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")

    # Detect collision with food.
    if snake.head.distance(food) <= 15:
        score.eat_food()
        snake.extend()
        food.refresh()

    # Detect collision with wall.
    if round(snake.head.xcor()) > 380 or round(snake.head.xcor()) < -380 \
            or round(snake.head.ycor()) > 280 or round(snake.head.ycor()) < -280:
        score.game_over()
        game_is_on = False

    # Detect collision with tail.
    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False

my_screen.exitonclick()
