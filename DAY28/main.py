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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , Text = "00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 ==0:
        #if its the 8th rep:
        count_down(long_break_sec)
        timer_label.config(text= "Break" ,fg=RED)
    elif reps % 2 ==0:
        #if its 2nd,4th,6th rep
        count_down(short_break_sec)
        timer_label.config(text= "Break" ,fg=PINK)
    else:
        #IF its the 1st,3rd,5th,and 7th:
        count_down(work_sec)
        timer_label.config(text= "Work", fg=GREEN,)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count /60 )
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #here we did dynamic typing we can do this only in python and not in other languages (after assigning the different value)  
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


#Canvas wedght is used for put image into the screen 
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="day28//tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,112,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)


#timer label 
timer_label = Label(text= "Timer" ,font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(row=1,column=2)
timer_label.config(padx=5,pady=3)

# start button
button = Button(text="Start",command=start_timer,highlightthickness=0)
button.grid(row=3,column=1)
button.config(padx=3,pady=2)

# reset button
button = Button(text="Reset",command=reset_timer,highlightthickness=0)
button.grid(row=3,column=3)
button.config(padx=3,pady=2)

#right tickmark label
tick_label = Label(text="",font=(FONT_NAME,15),fg=GREEN,bg=YELLOW)
tick_label.grid(row=4,column=2)
tick_label.config(padx=5,pady=5)



window.mainloop()