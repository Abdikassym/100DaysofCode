from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)  # Can be implemented into other components


def button_click():
    my_label["text"] = input.get()


# Creating a Label
my_label = Label(text="I am a Label", font=("Courier", 22, "bold"))

my_label["text"] = "New text"  # This is how we change or update a particular property in a component
my_label.config(text="New text 2.")  # These are two variants of the changing values in particular keys.

my_label.grid(column=0, row=0)


# Creating a Button
button = Button(text="First Button", command=button_click)
button.grid(column=1, row=1)

button2 = Button(text="Second Button")
button2.grid(column=2, row=0)
# Creating an Entry
input = Entry()
input.grid(column=3, row=2)



























# # Creating a text box
# text = Text(width=30, height=5)
# text.pack()
# text.focus()
# text.insert(END, "Multiline text box, for everything you want to write.")
#
#
# # Spin box
# def spinbox_used():
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=1000, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if button checked, else prints 0
#     print(checked_state.get())
# # variable to hold on to check state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radio button
# def radio_used():
#     print(radio_state.get())
#
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
# radiobutton2.pack()
# radiobutton1.pack()
#
# # List Box
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()
