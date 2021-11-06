from random import *
from tkinter import *
import pandas

try:
    words_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("words.csv")

BACKGROUND_COLOR = "#B1DDC6"


# --------------- FUNCTIONS ------------
to_learn = words_data.to_dict(orient="records")
print(to_learn)


def next_card():
    global current_card, flip_timer
    flip_timer = window.after(3000, func=flip_card)
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    front_card.itemconfig(language_title, text="English", fill="black")
    front_card.itemconfig(current_word, text=current_card["english"], fill="black")
    front_card.itemconfig(canvas, image=front_card_image)


def flip_card():
    front_card.itemconfig(canvas, image=back_card_image)
    front_card.itemconfig(language_title, text="Russian", fill="white")
    front_card.itemconfig(current_word, text=current_card["russian"], fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()

# --------------- UI DESIGN ------------
window = Tk()
window.title("English Language Learning Flashcards")
window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)

front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas = front_card.create_image(400, 263, image=front_card_image)
front_card.grid(column=0, row=0, columnspan=2)

language_title = front_card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
current_word = front_card.create_text(400, 263, text="", font=("Ariel", 24, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


# -----------Инструкция-------------
# Если пользователь знает слово, то он жмет галочку, и это слово не должно появляться в этой игре еще раз
# Если пользователь не знает слово, то оно уходит в новую таблицу words_to_learn.csv
# Когда пользователь открывает программу, то должна открываться игра со словами из файла words_to_learn
# Если этого файла нет, то открывается изначальный файл words.csv
next_card()



window.mainloop()

result_data = pandas.DataFrame(to_learn)
result_data.to_csv("words_to_learn.csv")
