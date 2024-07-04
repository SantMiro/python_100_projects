###############################
# Title: Flashcard App        #
# Author: Santiago Miro       #
#       July 2024             #
###############################

'''
This app performs as a learning tool to memorize 100 french words.
The user has 5 seconds to identofy the word or it is reshuffled back into the deck.
If user identifies word, it is removed from deck.
If user does not know word can skip it and word will be reshuffled.
'''
# Import libraries
from tkinter import * 
import pandas as pd
import random

# ------------------------------- START GAME  -------------------------------- #
def start_game(): # The list of words is shuffled and shows starting word. 
    global word_index, timer_id, paired_words
    random.shuffle(paired_words)
    word_index = 0
    if timer_id is not None: # It also restarts app if called again.
        window.after_cancel(timer_id)
        timer_id = None
    show_french_word() # Shows starting word

# ------------------------------- SHOW FRENCH WORD -------------------------------- #
def show_french_word(): # It shows the current word on the list. 
    global word_index, timer_id
    try:
        text = paired_words[word_index][0]
    except:
        canvas.itemconfig(word_display,text='You finished the game!', font=('Courier',18,'bold'))
    else:
        canvas.itemconfig(language_display,text='French: ')
        canvas.itemconfig(word_display,text=text)
        timer_id = count_down(5, show_english_word) # It starts 5 seconds count down for decision.

# ------------------------------- SHOW ENGLISH WORD  -------------------------------- #
def show_english_word(): # Shows translation of previously shown french word.
    global word_index, paired_words, timer_id, remove_word, removed_words
    canvas.itemconfig(language_display,text='English: ')
    canvas.itemconfig(word_display,text=paired_words[word_index][1])
    if remove_word:
        try:
            word_to_remove = paired_words.pop(word_index) # If word was known it is removed from list.
        except:
            canvas.itemconfig(word_display,text='You finished the game! Press Start New Game to start over.', font=('Courier',18,'bold'))
        else:
            removed_words.append(word_to_remove)
            remove_word = False
    random.shuffle(paired_words) # Reshuffle again remaining words.
    timer_id = count_down(1, next_french_word) # Count down 1 second to show next word

# ------------------------------- COUNT DOWN  -------------------------------- #
def count_down(count_segs,next_function): # Sets timer to count down seconds.
    global timer_id
    if count_segs >= 0 :
        timer_label.config(text = f'0:0{count_segs}')
        timer_id =window.after(1000, count_down, count_segs -1, next_function )
    else:
        next_function() # Calls next function after count down.
# ------------------------------- SHOW NEXT WORD  -------------------------------- #
def next_french_word(): # Shows next word on list
    global word_index
    show_french_word()

# ------------------------------- CONFIRM WORD  -------------------------------- #
def confirm_word(): # If word is known remove from list
    global timer_id, remove_word
    remove_word = True
    if timer_id is not None:
        window.after_cancel(timer_id) 
        temp_background('#B5C99A',BG) # Show flash of green background       
        show_english_word() # Show translation

# ------------------------------- PASS WORD  -------------------------------- #
def pass_word(): # If word is unknow skip word.
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        temp_background('#862B0D',BG) # Background flashes red
        show_english_word() # Show translation

# ------------------------------- BACKGROUND COLOR -------------------------------- #
def restore_background_color(bg_color): # Return to default background color
    window.config(bg=bg_color)
    canvas.config(bg=bg_color)
    timer_label.config(bg=bg_color)
    button_canvas.config(bg=bg_color)

def temp_background(color,default_bg): # Memontarily change background colors
    window.config(bg=color)
    canvas.config(bg=color)
    timer_label.config(bg=color)
    button_canvas.config(bg=color)
    window.after(100, lambda: restore_background_color(default_bg))


# ------------------------------- GLOBAL CONSTANTS -------------------------------- #
words = pd.read_csv('day30_flashcards_en_fr/fr_100words_en.csv') # Call csv with words.
paired_words = [(row.French,row.English) for (_,row) in words.iterrows()] # Set pairs of translated and original
word_index = 0
timer_id = None
remove_word = False
removed_words = [] # List of removed words.

BG = '#F9E0BB' # Brownish background
BUTTON_BG = '#C38154' # Dark brown color
FONT_LABEL = ('Courier',40,'bold') 
FONT_BUTTON = ('Courier',18,'normal')

# ------------------------------- UI DESIGN -------------------------------- #
# WINDOW
window = Tk()
window.title('Flascards App')
window.config(padx=50,pady=50, bg=BG)

# CANVAS
canvas = Canvas(width=630, height=430, highlightthickness=0, bg=BG)
scroll_img = PhotoImage(file='day30_flashcards_en_fr/scroll.png')
canvas.create_image(315,215,image=scroll_img)
language_display = canvas.create_text(200,150,text='',font=('Courier',20,'normal'))
word_display = canvas.create_text(315,215,text='',font=FONT_LABEL)
canvas.grid(column=0, row=0, columnspan=3)

# LABELS
timer_label = Label(text='0:00', font=FONT_LABEL, bg=BG)
timer_label.grid(column=3, row=0)

# BUTTONS
button_canvas = Canvas(width=630,height=60, highlightthickness=0, bg=BG)
button_canvas.grid(column=0,row=1,columnspan=3)

# confirm button
correct_circle = button_canvas.create_oval(473-30,0,473+30,60, fill=BUTTON_BG,outline=BUTTON_BG)
correct_button = Button(button_canvas,text='✔',fg='#B5C99A',font=FONT_BUTTON,bd=0, highlightthickness=0,bg=BUTTON_BG, command=confirm_word)
button_canvas.create_window(473, 30, window=correct_button)

# pass button
pass_circle = button_canvas.create_oval(158-30,0,158+30,60, fill=BUTTON_BG,outline=BUTTON_BG)
pass_button = Button(button_canvas,text='✘',fg='#862B0D',font=FONT_BUTTON,bd=0, highlightthickness=0,bg=BUTTON_BG, command=pass_word)
button_canvas.create_window(158, 30, window=pass_button)

#start button
start_button = Button(text='Start Game',font=FONT_BUTTON, bg= BUTTON_BG, command=start_game)
start_button.grid(column=3,row=1)


window.mainloop()