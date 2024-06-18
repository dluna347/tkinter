from tkinter import *

# function to convert miles to Km
def miles_to_km(n):
    """n = number of miles"""
    kilometers = n * 1.60934
    return int(kilometers)

# function to clear "Enter Miles here"
def clear_entry(event):
    if input.get() == "Enter Miles":
        input.delete(0, END)

def on_calculate():
    try:
        value = float(entry_var.get())
        kilometers = miles_to_km(value)
        label_result.config(text=str(kilometers))
    except ValueError:
        label_result.config(text="Invalid input")

# setup tkinter
main_window = Tk()
main_window.title("Mile to Km Converter")
main_window.resizable(False, False)

# create a StringVar to hold the entry data
entry_var = StringVar()

# create an Entry box for the user to enter the number of miles
input = Entry(textvariable=entry_var)
input.grid(row=0, column=0, padx=10, pady=10)
input.insert(0, "Enter Miles")
input.bind("<FocusIn>", clear_entry)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=1, padx=5, pady=10)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0, padx=10, pady=5)

label_result = Label(text="")
label_result.grid(row=1, column=1, padx=5, pady=5)

label_km = Label(text="Km")
label_km.grid(row=1, column=2, padx=5, pady=5)

calculate = Button(text="Calculate", command=on_calculate)
calculate.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

main_window.mainloop()