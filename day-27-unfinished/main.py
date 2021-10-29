from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)


# Creating a Label
my_label = Label(text="I am a Label", font=("Courier", 32, "bold"))
my_label.pack()

my_label["text"] = "New text"  # This is how we change or update a particular property in a component
my_label.config(text="New text 2.")  # These are two variants of the changing values in particular keys.



# Creating a Button
def button_click():
    my_label["text"] = input.get()


button = Button(text="Click me", command=button_click)
button.pack()


# Creating an Entry
input = Entry()
input.pack()


# Creating a text box
text = Text(width=30, height=5)
text.pack()
text.focus()
text.insert(END, "Multiline text box, for everything you want to write.")


# Spin box
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



window.mainloop()
