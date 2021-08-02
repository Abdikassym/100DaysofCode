#Step 1 
import random
import hangman_art
import hangman_words
from replit import clear

word_list = ["ardvark", "baboon", "camel"]
answer = random.choice(hangman_words.word_list)
display = []
lives = 6

print(hangman_art.logo)

for i in range(len(answer)):
  display += "_"

end_of_game = False

while not end_of_game:
  
  guess = input("Guess the letter: ").lower()

  clear()

  if guess in display:
      print('This guess is already in your answer. Try again.')
  else:
    for letter in range(len(answer)):
      
      if guess == answer[letter]:
        display[letter] = guess
    
    print(" ".join(display))

    if guess not in answer:
      lives -= 1
      print(hangman_art.stages[lives])
      print(f"{guess} is not in a word")
    else:
      print(hangman_art.stages[lives])
      print(f"'{guess}' is in a word")

    if "_" not in display:
      print(f"You won! The final answer was - {answer}.")
      end_of_game = True
      
    if lives == 0:
      print(f"Game over. The final answer was - {answer}.")
      end_of_game = True
  
  print('\n')