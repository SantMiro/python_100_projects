from tkinter import Tk
from ui import QuizAppUI
from logic import QuizzLogic

if __name__ == '__main__':
    window = Tk()
    logic = QuizzLogic(None)  # Temporarily set to None
    app = QuizAppUI(window, logic)
    logic.ui = app  # Assign the UI to the logic
    window.mainloop()