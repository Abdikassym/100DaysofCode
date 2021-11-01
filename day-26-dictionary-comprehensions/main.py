import pandas

student_dict = {
    "student": ["Angela", "James", "Nick"],
    "scores": [56, 76, 98]
}

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letters = {code["letter"]: code["code"] for index, code in data.iterrows()}
# print(letters)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word: ").upper()

nato_code = [letters[i] for i in user]
print(nato_code)
