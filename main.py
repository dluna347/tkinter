from tkinter import *


# function to convert miles to Km
def miles_to_km(n):
    """n = number of miles"""
    kilometers = n * 1.60934
    return kilometers

# function to clear "Enter Miles here"
def clear_entry(event):
    if input.get() == "Enter Miles":
        input.delete(0, END)

def on_enter_press(event):
    pass

# setup tkinter
main_window = Tk()
main_window.minsize(600, 300)
main_window.title("Mile to Km Converter")
main_window.resizable(False, False)

# create an Entry box for the user to enter the number
# of miles to be converted to Km
# and elete "Enter Miles here" once it gets clicked (goes with function 1)
input = Entry()
input.grid(column=3, row=1)
input.insert(string="Enter Miles", index=0)
input.bind("<FocusIn>", clear_entry)

label = Label(text="Miles")
label.grid(row=1, column=4)


label_2 = Label(text="is equal to")
label_2.grid(row=3, column=1)


label_3 = Label(text=0)
label_3.grid(row=3, column=2)

label_4 = Label(text="Km")
label_4.grid(row=3, column=3)

text = input.get()

print(text)












main_window.mainloop()


# continue here:

# input needs to be converted using the miles_to_km function
# and then passed onto label_3