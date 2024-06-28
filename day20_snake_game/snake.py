from turtle import Turtle, Screen

STARTING_POSITION = [(-20,0), (-40,0), (-60,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake():

    def __init__(self):
        self.squares = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITION:
            self.segment(position)

    def segment(self,position):
        square = Turtle(shape = 'square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def increase_size(self):
        self.segment(self.squares[-1].pos())

    def move(self):

        for square in range(len(self.squares)-1,0,-1):
            new_X = self.squares[square -1].xcor()
            new_y = self.squares[square -1].ycor()
            self.squares[square].goto(new_X,new_y)
        self.squares[0].forward(MOVE_DISTANCE)


    def reset(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    
        
