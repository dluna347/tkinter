from tkinter import *
import random


password_chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',',
    '.', '<', '>', '?', '/'
]







# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    rand_list = []
    random_choice = random.choices(password_chars, k=12)
    joined_string = ''.join(random_choice)
    return joined_string

def update_entry():
    password_entry.insert(0, password())
# ---------------------------- SAVE PASSWORD ------------------------------- #
# take all the inputs and once the user clicks on add, save the data to data.txt
# afterwards, wipe clear the info on the app

def save():
    with open(file="./data.txt", mode="a") as file:
        file.write(f"Website: {website_entry.get()}")
        file.write("\n")
        file.write(f"username: {email_username_entry.get()}")
        file.write("\n")
        file.write(f"Password: {password_entry.get()}")
        file.write("\n")
        file.write("\n")
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)

        

   
    
    



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


image = PhotoImage(file="logo.png")


canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0,column=1)

# labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "dion.luna2081@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
# Buttons
generate_pw_button = Button(text="Generate Password", command=update_entry)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()


