from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def calculate():
    km["text"] = int(input.get()) * 1.609


input = Entry(width=7)
input.grid(column=1, row=0)
# input.config(padx=10, pady=10)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

km = Label(text=0)
km.grid(column=1, row=1)
km.config(padx=10, pady=10)


kilometers = Label(text="Km")
kilometers.grid(column=2, row=1)
kilometers.config(padx=10, pady=10)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
# button.config(padx=10, pady=10)

window.mainloop()
