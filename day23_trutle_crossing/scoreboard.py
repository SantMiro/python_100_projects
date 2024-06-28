from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier',20,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0,250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Levels crossed: {self.score}', align= ALIGN, font= FONT)

    def level_passed(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.teleport(0,0)
        self.write('GAME OVER', align=ALIGN, font=FONT)