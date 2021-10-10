invited = []

with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file.readlines():
        invited.append(name.strip())


with open("Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()


for i in invited:
    with open(f"letter_for_{i}", "w") as person:
        person.write(starting_letter.replace("[name]", i))
