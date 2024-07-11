import requests
import html

class QuizzLogic:
    def __init__(self,ui):
        self.ui = ui
        self.questions = []
        self.counter = 0
        self.score = 0
        self.question_display = []
        self.game_over = False
        self.correct_answer = ""
        self.label = None


    def start_game(self):
        self.game_over = False
        self.clear_text()
        self.questions = self.get_data()
        self.counter = 0
        self.score = 0
        self.ui.score_label.config(text=f'Score: {self.score}')
        self.show_question()

    # ------------------------------- SHOW QUESTION -------------------------------- #
    def show_question(self):
        self.clear_text()
        try:
            question = self.questions[self.counter]['question']
        except:
            self.end_game()
        else:
            self.correct_answer = self.questions[self.counter]['correct_answer']
            self.counter += 1
            max_length = 38  # Max length of characters per line
            lines = self.split_text(question, max_length)
            for text in self.question_display:
                self.ui.canvas.delete(text)  # Remove the existing text
            self.question_display = []  # Reset the question_display to store new text items
            for i, line in enumerate(lines):
                text_id = self.ui.canvas.create_text(200, 120 + i*20, text=line, font=self.QUESTION_FONT)
                self.question_display.append(text_id)

    # ------------------------------- USER ANSWER -------------------------------- #
    def user_answer(self,answer):
        if self.correct_answer == answer:
            self.temp_background('#97BE5A','white')
            self.score += 1
            self.ui.score_label.config(text=f'Score: {self.score}') 
            self.show_question()
        else:
            self.temp_background('#FF0000','white')
            self.show_question()

    # ------------------------------- TRUE BUTTON -------------------------------- #
    def correct(self):
        if not self.game_over:
            self.user_answer('True')

    # ------------------------------- FALSE BUTTON -------------------------------- #
    def incorrect(self):
        if not self.game_over:
            self.user_answer('False')

    # ------------------------------- END GAME -------------------------------- #
    def end_game(self):
        self.game_over = True
        self.clear_text()
        self.label = self.ui.canvas.create_text(200, 120, text=f'Game Over\nTotal Score: {self.score}', font=self.SCORE_FONT)

    def clear_text(self):
        for text in self.question_display:
            self.ui.canvas.delete(text)
        self.question_display = []
        if self.label is not None:
            self.ui.canvas.delete(self.label)
            self.label = None

    # ------------------------------- BACKGROUND COLOR -------------------------------- #
    def restore_background_color(self,bg_color): # Return to default background color
        self.ui.canvas.config(bg=bg_color)

    def temp_background(self,color,default_bg): # Memontarily change background colors
        self.ui.canvas.config(bg=color)
        self.ui.window.after(100, lambda: self.restore_background_color(default_bg))

    # ------------------------------- BACKGROUND COLOR -------------------------------- #
    def split_text(self,text, max_length):
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
    
    def get_data(self):
            response = requests.get(f'https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean')
            response.raise_for_status()
            data = response.json()

            questions = data['results']
            for question in questions:
                question['question'] = html.unescape(question['question'])
            return questions

    QUESTION_FONT = ('Courier',12,'normal')
    SCORE_FONT = ('Courier',20,'normal')
    BACKGROUND_COLOR = '#FFE8C5'
    BUTTON_COLOR = '#FFA27F'
