from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

run = True

def caesar(text, shift, direction):
  new_text = ""

  if shift > 26:
    shift = shift % 26
  if direction == "decode":
      shift = -shift 
  for i in text: #mjqqt
    if i not in alphabet:
      new_text += i
    else:
      current_position = alphabet.index(i)
      new_position = current_position + shift
      new_text += alphabet[new_position]
  
  print(f"This is your cipher - {new_text}\n")

while run:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  restart = input("Do you want to lauch programm once again? yes/no ")
  if restart == "no":
    print("Thank you and goodbye.")
    run = False



