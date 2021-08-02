#1. Create a greeting for your program.
print('Greeting, rocker!')
#2. Ask the user for the city that they grew up in.
user_city = input('Which city are you from?\n')
#3. Ask the user for the name of a pet.
user_pet = input('What is the name of you pet?\n')
#4. Combine the name of their city and pet and show them their band name.
band_name = user_city + ' ' + user_pet
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
print("Your band's name is " + band_name)
