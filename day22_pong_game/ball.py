from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.ball_xspeed=15
        self.ball_yspeed=15


    def move(self):
        new_x = self.xcor() + self.ball_xspeed
        new_y = self.ycor() + self.ball_yspeed
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.ball_yspeed = -self.ball_yspeed

    def paddle_bounce(self):
        self.ball_xspeed = -self.ball_xspeed

        