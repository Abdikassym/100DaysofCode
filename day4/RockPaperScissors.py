import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possibilities = [rock, paper, scissors]
computer = random.choice(possibilities)

player = int(input("Choose your fighter 1 as Rock, 2 as Paper, 3 as Scissors\n"))
if player < 1 or player > 3:
  print('Invalid number, try again.')
else:
  if player == 1:
    print("You chose rock!\n", rock)
  elif player == 2:
    print("You chose paper!\n", paper)
  else:
    print("You chose scissor!\n", scissors)

  if computer == rock:
    print(f"Computer chose rock!\n", computer)
  elif computer == paper:
    print(f"Computer chose paper!\n", computer)
  else:
    print(f"Computer chose scissors!\n", computer)
    
  if player == 1:
    if computer == rock:
      print("Draw!")
    elif computer == paper:
      print("Lose!")
    else:
      print("Win!")

  elif player == 2:
    if computer == rock:
      print("Win!")
    elif computer == paper:
      print("Draw!")
    else:
      print("Lose!")

  else:
    if computer == rock:
      print("Lose!")
    elif computer == paper:
      print("Win!")
    else:
      print("Draw!")