from tkinter import *
from PIL import Image, ImageTk


class QuizAppUI:
    def __init__(self,window,logic):
        self.window = window
        self.logic = logic
        self.window.title('Quizz_app')
        self.window.config(padx=20,pady=20, bg=self.BACKGROUND_COLOR)

        # CANVAS
        self.canvas = Canvas(width = 400, height=300, highlightthickness=0, )
        self.canvas.grid(column=0, row=1, columnspan=3)
        #self.label = None

        # LABELS
        self.score_label = Label(text=f'Score: {self.logic.score}', bg=self.BACKGROUND_COLOR,font=self.SCORE_FONT)
        self.score_label.grid(column=2, row=0, padx=20,pady=20)

        # BUTTONS
        # CHECK MARK
        self.check_mark_img = self.load_image('check_mark.png',(100,100))
        self.correct_button = Button(image=self.check_mark_img, bg=self.BUTTON_COLOR,command=self.logic.correct)
        self.correct_button.grid(column=2,row=2, padx=20, pady=20)

        # RED CROSS
        self.red_cross_img = self.load_image('red_cross.png',(100,100))
        self.incorrect_button = Button(image=self.red_cross_img, bg=self.BUTTON_COLOR,command=self.logic.incorrect)
        self.incorrect_button.grid(column=0,row=2, padx=20, pady=20)

        # NEW GAME 
        self.new_game = Button(text='New Game',font=self.SCORE_FONT,command=self.logic.start_game)
        self.new_game.grid(column=0,row=0)

    def load_image(self,path,size):
        original = Image.open(path)
        resized = original.resize(size)
        return ImageTk.PhotoImage(resized)

    SCORE_FONT = ('Courier',20,'normal')
    BACKGROUND_COLOR = '#FFE8C5'
    BUTTON_COLOR = '#FFA27F'
            