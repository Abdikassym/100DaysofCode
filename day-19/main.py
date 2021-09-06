from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

colors = ["green", "purple", "pink", "red", "blue", "darkblue", "orange"]
participants = ["Sardar", "Dyas", "Aiin", "Azeazy", "Alen", "Anuka", "Yerlan"]
y_positions = [270, 180, 90, 0, -90, -180, -270]
all_turtles = []

game_is_on = False

user_bet = screen.textinput(title="Choose you fighter: ", prompt="Welcome to an Elite Race! Choose you "
                                                                 "Elite Club member to finish the race first! "
                                                                 "Good Luck!")
if user_bet:
    game_is_on = True


for cherepashka in range(0, 7):
    tim = Turtle()
    tim.name = participants[cherepashka]
    tim.shape("turtle")
    tim.color(colors[cherepashka])
    tim.penup()
    tim.setpos(-380, y_positions[cherepashka])
    tim.write(participants[cherepashka], move=False, align="left", font=("Arial", 16, "normal"))
    tim.speed(1)
    tim.fd(75)
    tim.pendown()
    tim.speed(0)
    all_turtles.append(tim)

line = Turtle()
line.penup()
line.goto(250, 300)
line.setheading(270)
line.pendown()
line.forward(600)


while game_is_on:
    for member in all_turtles:
        if member.xcor() >= 235:
            game_is_on = False
            winner = member
            winner.write(f"Winner!", align="left", move=False, font=("Arial", 24, "normal"))
        else:
            random_dist = random.randint(0, 10)
            member.forward(random_dist)


if user_bet == winner.name:
    print(f"You have won! {winner.name} is in fact a winner!")
else:
    print(f"Oh no, you lost! The real winner is {winner.name}!")
    print(f"{user_bet} was so close!")


screen.exitonclick()
