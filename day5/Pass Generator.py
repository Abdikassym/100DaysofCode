#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_total = nr_letters + nr_numbers + nr_symbols

all_symbols = [letters, numbers, symbols]


password = ""


while nr_total > 0:
  new = ""
  new = random.choice(random.choice(all_symbols))
  
  if nr_total > 0:
    if new in letters and nr_letters > 0:
      nr_letters -= 1
      nr_total -= 1
      
      password += new
    if new in numbers and nr_numbers > 0:
      nr_numbers -= 1
      nr_total -= 1
      
      password += new
    if new in symbols and nr_symbols > 0:
      nr_symbols -=1
      nr_total -= 1

      password += new

print(password)


# for i in range(nr_letters + nr_numbers + nr_symbols):
#   hard_password

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P