from tkinter import *
import math

LIGHT_GREEN = '#EDF1D6'
GREEN = '#9DC08B'
DARK_GREEN = '#9DC08B'
DARKEST_GREEN = '#40513B'

FONT = ('Courier',50,'bold')
FONT_BUTTON = ('Helvetica',20,'normal')
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer,text='00:00')
    label.config(text='Timer')
    check.config(text='')
    global reps
    reps = 0


def start_time():
    global reps 
    reps += 1
    
    if reps % 8 == 0:
        count_down(20*60)
        label.config(text = 'Break', fg=DARK_GREEN)
    elif reps % 2 == 0:
        count_down(5*60)
        label.config(text= 'Small Break', fg=GREEN)
    else:
        count_down(300)
        label.config(text='Timer',font = FONT,fg=DARKEST_GREEN,bg=LIGHT_GREEN)


def count_down(count):
    count_mins = math.floor(count / 60)
    count_segs = count % 60
    if count_segs == 0:
        canvas.itemconfig(text_timer, text = f'{count_mins}:00')
    else:
        canvas.itemconfig(text_timer, text = f'{count_mins}:{count_segs}')
    if count > 0 :
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        mark = str()
        for _ in range(math.floor(reps/2)):
            mark += '✔'
        check.config(text=mark)

window = Tk()
window.title('Pomodoro')
window.config(padx=50,pady=50, bg = LIGHT_GREEN)

label = Label(text = 'Timer', font = FONT,fg=DARKEST_GREEN,bg=LIGHT_GREEN)
label.grid(column=1,row=0)

canvas = Canvas(width = 550, height= 550, bg = LIGHT_GREEN)
tomato_img = PhotoImage(file='day28_pomodoro_app/tomato-icon.png')
canvas.create_image(270,255,image = tomato_img)
text_timer = canvas.create_text(270, 270, fill = 'white', text = '00:00', font = FONT)
canvas.grid(column=1, row= 1)

start_button = Button(text = 'Start',command=start_time, bg=DARKEST_GREEN,fg= LIGHT_GREEN, font = FONT_BUTTON)
start_button.grid(column=0, row=2)

check = Label( font= FONT, fg= DARKEST_GREEN, bg=LIGHT_GREEN)
check.grid(column=1,row=2)

reset_button = Button(text = 'Reset',bg=DARKEST_GREEN,fg= LIGHT_GREEN, font = FONT_BUTTON, command=reset_timer)
reset_button.grid(column=2, row=2)







window.mainloop()