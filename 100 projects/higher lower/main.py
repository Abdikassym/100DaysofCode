import random
from art import logo, vs
from game_data import data
import replit

game_over = False
score = 0

first = random.choice(data)
data.remove(first)

def answer(first, second):
    if first["follower_count"] > second["follower_count"]:
      # print(f"{first['name']} has more with {first['follower_count']}")
      return "a"
    else:
      # print(f"{second['name']} has more with {second['follower_count']}")
      return "b"

replit.clear()
print(logo)

while not game_over:
  if len(data) < 2:
    print("There are no more accounts left. You won!")
    game_over = True
    
  print(f"""Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}.""")
  print(vs)

  second = random.choice(data)
  print(f"""Compare B: {second["name"]}, a {second["description"]}, from {second["country"]}.""")
  data.remove(second)

  winner = answer(first, second)
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  if choice == winner:
    replit.clear()
    print(logo)
    score += 1
    print(f"You are right! Your current score: {score}.")

    first = second
  else:
    replit.clear()
    print(logo)
    print(f"Sorry, that is wrong. Final score: {score}.")
    game_over = True
