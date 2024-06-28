from turtle import Turtle

STARTING_POSITION = (0,-280)
CROSSING_SPEED = 20
CLOCK_SPEED = 0.1

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.clock_speed = CLOCK_SPEED

    def up(self):
        new_y = self.ycor() + CROSSING_SPEED
        self.goto(0,new_y)

    def down(self):
        new_y = self.ycor() - CROSSING_SPEED
        self.goto(0,new_y)

    def level_passed(self):
        self.goto(STARTING_POSITION)
        self.clock_speed *= 0.9
        
