import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for i in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for k in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for j in range(randint(2, 4))]

    password_list = pass_numbers + pass_symbols + pass_letters

    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(END, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = web_input.get()
    username = user_input.get()
    password = pass_input.get()

    new_data = {
        f"{website}": {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error occurred.", message="No empty inputs are available. Please refill data.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Information", message=f"Do you confirm written data?\n\n"
                                                                            f"Website:  {website}\n"
                                                                            f"Username:  {username}")
        if is_ok:
            messagebox.showinfo(title="Success!", message="Information has been saved correctly.")
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                web_input.delete(0, "end")
                user_input.delete(0, "end")
                pass_input.delete(0, "end")


def search():
    website = web_input.get()

    try:
        with open("data.json", "r") as data_file:
            current_data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message=f"File has not been found. Try to create one first.")

    else:
        if website in current_data:
            current_website = current_data[website]["email"]
            current_password = current_data[website]["password"]
            messagebox.showinfo(title="User information",
                                message=f"Email: {current_website}\nPassword: {current_password}")
        else:
            messagebox.showerror(title="Oops", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_input = Entry(width=36)
web_input.focus()
web_input.grid(column=1, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_input = Entry(width=56)
user_input.insert(END, "example@exmaple.com")
user_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=37)
pass_input.config()
pass_input.grid(column=1, row=3)

pass_generate = Button(text="Generate Password", width=15, command=generate_password)
pass_generate.grid(column=2, row=3)

add_button = Button(text="Add", width=47, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
