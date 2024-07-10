from tkinter import *
from data import get_data
from PIL import Image, ImageTk
import html
QUESTION_FONT = ('Courier',12,'normal')
SCORE_FONT = ('Courier',20,'normal')
BACKGROUND_COLOR = '#FFE8C5'
BUTTON_COLOR = '#FFA27F'

score = 0
question_display = []
game_over = False

# ------------------------------- START GAME -------------------------------- #
def start_game():
    global questions, counter, score, question_display, game_over
    game_over = False
    try:
        canvas.itemconfig(label, text='')
    except:
        pass
    
    questions = get_data()
    counter = 0
    score = 0
    show_question()

# ------------------------------- SHOW QUESTION -------------------------------- #
def show_question():
    global counter, question_display, correct_answer
    try:
        question = questions[counter]['question']
    except:
        end_game()
    else:
        correct_answer = questions[counter]['correct_answer']
        counter += 1
        max_length = 38  # Max length of characters per line
        lines = split_text(question, max_length)
        for text in question_display:
            canvas.delete(text)  # Remove the existing text
        question_display = []  # Reset the question_display to store new text items
        for i, line in enumerate(lines):
            text_id = canvas.create_text(200, 120 + i*20, text=line, font=QUESTION_FONT)
            question_display.append(text_id)

# ------------------------------- USER ANSWER -------------------------------- #
def user_answer(answer):
    global score
    if correct_answer == answer:
        temp_background('#97BE5A','white')
        score += 1
        score_label.config(text=f'Score: {score}') 
        show_question()
    else:
        temp_background('#FF0000','white')
        show_question()

# ------------------------------- TRUE BUTTON -------------------------------- #
def correct():
    if not game_over:
        user_answer('True')

# ------------------------------- FALSE BUTTON -------------------------------- #
def incorrect():
    if not game_over:
        user_answer('False')

# ------------------------------- END GAME -------------------------------- #
def end_game():
    global game_over, label
    game_over = True
    for text in question_display:
        canvas.delete(text)
    label = canvas.create_text(200, 120, text=f'Game Over\nTotal Score: {score}', font=SCORE_FONT)

# ------------------------------- BACKGROUND COLOR -------------------------------- #
def restore_background_color(bg_color): # Return to default background color
    canvas.config(bg=bg_color)

def temp_background(color,default_bg): # Memontarily change background colors
    canvas.config(bg=color)
    window.after(100, lambda: restore_background_color(default_bg))

# ------------------------------- BACKGROUND COLOR -------------------------------- #
def split_text(text, max_length):
    """Splits text into multiple parts if it exceeds max_length"""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) <= max_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    return lines

# -------------------------UI DESIGN -----------------------------#
# WINDOW
window = Tk()
window.title('Quizz_app')
window.config(padx=20,pady=20, bg=BACKGROUND_COLOR)

# CANVAS
canvas = Canvas(width = 400, height=300, highlightthickness=0, )
canvas.grid(column=0, row=1, columnspan=3)

# LABELS
score_label = Label(text=f'Score: {score}', bg=BACKGROUND_COLOR,font=SCORE_FONT)
score_label.grid(column=2, row=0, padx=20,pady=20)

# BUTTONS
# CHECK MARK
check_mark_original = Image.open('check_mark.png')
check_mark_resized = check_mark_original.resize((100, 100))  # Resize to 100x100 pixels
check_mark_img = ImageTk.PhotoImage(check_mark_resized)
correct_button = Button(image=check_mark_img, bg=BUTTON_COLOR,command=correct)
correct_button.grid(column=2,row=2, padx=20, pady=20)

# RED CROSS
red_cross_original = Image.open('red_cross.png')
red_cross_resized = red_cross_original.resize((100, 100))  # Resize to 100x100 pixels
red_cross_img = ImageTk.PhotoImage(red_cross_resized)
incorrect_button = Button(image=red_cross_img, bg=BUTTON_COLOR,command=incorrect)
incorrect_button.grid(column=0,row=2, padx=20, pady=20)

# NEW GAME 
new_game = Button(text='New Game',font=SCORE_FONT,command=start_game)
new_game.grid(column=0,row=0)

start_game()

window.mainloop()