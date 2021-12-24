from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    label_checkmark.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 8:
        count_down(long_break_sec)
        label_title.config(text="Long Break", fg=RED)
    #If it's 1., 3., 5., 7. rep:
    elif reps % 2 == 1:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)
    #If it's 2. 4. 6. rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)
    #If it's 8th






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    global timer

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            mark += "✓"
        label_checkmark.config(text=mark)








# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

button = Button(text="Reset", command=reset_timer)
button.grid(column=2, row=2)

label_title = Label(text="Timer",font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

label_checkmark = Label(font=(FONT_NAME,25,"bold"), fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

window.mainloop()
