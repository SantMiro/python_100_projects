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
        self.high_score = self.retrieve_high_score()
        self.update_score()
        
    def update_score(self):
        self.write(f'Score: {self.score} -  High Score: {self.high_score}',align=ALIGN,font=FONT)

    def score_point(self):
        self.clear()
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.update_score()
        self.save_high_score()
        
    
    def save_high_score(self):
        with open('high_score.txt','w') as f:
            high_score = str(self.high_score)
            f.write(high_score)

    def retrieve_high_score(self):
        with open('high_score.txt','r') as f:
            high_score = int(f.read())
            return high_score

    def game_over(self):
        self.teleport(0,0)
        self.write('GAME OVER!',align=ALIGN,font=FONT)
        