from player import Player
from turtle import Screen
from car import Car
from time import sleep
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()

enemies = []
for unit in range(30):
    enemy = Car()
    enemies.append(enemy)

game_is_on = True

game_speed = 0.1
screen.listen()
while game_is_on:
    sleep(game_speed)
    screen.update()
    for unit in enemies:
        unit.move()
        if unit.distance(player) < 20:
            player.game_over()
            game_is_on = False
    screen.onkey(player.step, "Up")
    screen.onkey(player.step_left, "Left")
    screen.onkey(player.step_back, "Down")
    screen.onkey(player.step_right, "Right")

    if player.ycor() > 275:
        if game_speed == 0.01:
            pass
        else:
            game_speed -= 0.01
        player.next_round()
        score.add_score()















screen.exitonclick()
