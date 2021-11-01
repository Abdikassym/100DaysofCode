numbers = [1, 2, 3, 4, 5]
new_list = [i + 1 for i in numbers]

name = "Angela"
double_name = [i + i for i in name]

new_range = [i * 2 for i in range(1, 5)]

names = ["Alen", "Bruh", "Gera", "Chris", "Dyas", "Drimlite", "Anuka", "Sardar", "Elmar"]
short_names = [name.upper() for name in names if len(name) >= 5]

print(short_names)


