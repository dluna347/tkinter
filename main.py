import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.minsize(500, 300)
window.title("First Tkinter program")
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="This is a label", font=("arial", 16, "bold"))
# my_label.pack() 
# my_label.place(x=100,y=200)
my_label.grid(row=0, column=0)

# make the text different from the initial text that was displayed(look at handy_reference guide)
my_label["text"] = "hello, label updated"
my_label["fg"] = "blue"

# or
my_label.config(text="label")

# create an event listener
def button_clicked():
    my_label["text"] = input.get() #this is the .get attribute from the Entry method

# creating buttons

button = tkinter.Button()
button["text"] = "click me"
button["bg"] = "gray"
# use the tkinter property - command - to call the button_clicked function
button["command"] = button_clicked
# button.pack()
button.grid(row=1, column=1)

# create a second button
button_2 = tkinter.Button()
button_2["text"] = "new button"
button_2["bg"] = "orange"
button_2.grid(row=0, column=2)

# The entry component (a field to enter text)

input = Entry()
input.config(width=10)
input.insert(index=tkinter.END, string="Text to begin with")
# input.pack()
input.grid(row=2, column=3)



window.mainloop()

