from turtle import Turtle

PADDLE_SPEED = 30

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.create_paddle(position)

    
    def create_paddle(self,position):
        
        self.penup()
        self.setheading(90)       
        self.color('white')
        self.resizemode("user")
        self.shapesize(1, 5, 1)
        self.goto(position) 

    def up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.goto(self.xcor(),new_y)        