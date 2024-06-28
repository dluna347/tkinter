from tkinter import *
from datetime import timedelta
import math



def create_custom_button(root, button_text):
    return Button(
        root,
        text=button_text,
        bg='#4CAF50',
        fg='white',
        font=('Arial', 12),
        activebackground='#45a049',
        relief=FLAT,
        padx=10,
        pady=5
    )

reps = 0

    
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✅"
timer_start = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_start)
    timer.config(text="Timer")
    poms_completed.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # it it's the 1st/3rd/5th/7th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        # if it's 2nd/ 4th/ 6th rep:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    # to change a canvas element, tap into the particular canvas that you want to change
    # and then call the method itemconfig() and pass the particular item that you want to configure.
    # and then pass the thing about it that you want to change, in this case, the text.
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    # .after - executes a command after a time delay (in milliseconds, 1000 ms = 1 sec)
    # parameters: ms - amount of time, func=None, the function, *args - unlimited positional arguments
    if count > 0:
        global timer_start
        timer_start = window.after(1000, count_down, count - 1)
    else:
        if count == 0:
            start_timer() 
            mark = ""
            for _ in range(math.floor(reps/2)):
                mark += "✅"
                poms_completed.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)



# the canvas widget allows you to layer multiple things on top of each other.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)
# count_down(5)


timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=1, column=2)

start = Button(window, text="Start", command=start_timer)
start.grid(row=3, column=1)

reset = Button(window, text="Reset", command=reset_timer)
reset.grid(row=3, column=3)

poms_completed = Label(bg=YELLOW)
poms_completed.grid(row=4, column=2)

window.mainloop()

# add the following:
# label = Timer
# button = Start
# button = Reset
# label = keeps track of how many pomodoro's we've done.  each 25 minute session get's us one check mark




