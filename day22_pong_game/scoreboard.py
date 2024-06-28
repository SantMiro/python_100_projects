from turtle import Turtle
import time

ALIGN = 'center'
FONT = ('Courier',40,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(0,220)
        self.color('white')
        self.ht()
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()
        self.mid_field()    

    def update_score(self):
        #self.ht()
        self.clear()
        self.write(f'{self.p1_score}      {self.p2_score}',align = ALIGN, font = FONT)

    def score(self,ball):

        if ball.xcor() > 380:
            self.p1_score += 1
        elif ball.xcor() < -380:
            self.p2_score += 1
        self.update_score()
        time.sleep(2)
        ball.goto(0,0)
        ball.move_speed = 0.1

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align=ALIGN, font=FONT)

    def mid_field(self):
        division_line = Turtle(shape = 'square')
        division_line.color('white')
        division_line.penup()
        division_line.resizemode('user')
        division_line.shapesize(30, 0.5, 1)