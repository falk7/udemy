from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="25:00")
    check_marks.config(text="")
    title_label.config(text="Timer")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    count = 0
    if reps in [0, 2, 4, 6]:
        title_label.config(text="Work!", fg=GREEN)
        count = WORK_MIN
    if reps in [1, 3, 5]:
        title_label.config(text="Break!", fg=PINK)
        count = SHORT_BREAK_MIN
    if reps == 7:
        title_label.config(text="Break!", fg=RED)
        count = LONG_BREAK_MIN
    reps += 1
    count_down(count*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        check_marks.config(text="✔"*(reps//2))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 234/2, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white",
                                font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 36, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 36, "bold"))
check_marks.grid(column=1, row=4)

window.mainloop()
