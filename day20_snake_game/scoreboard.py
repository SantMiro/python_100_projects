from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',14,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(0,250)
        self.color('white')
        self.ht()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.write(f'Score: {self.score}',align=ALIGN,font=FONT)

    def score_point(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.teleport(0,0)
        self.write('GAME OVER!',align=ALIGN,font=FONT)
        