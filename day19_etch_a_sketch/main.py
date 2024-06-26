from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_clock():
    tim.right(10)

def rotate_anticlock():
    tim.left(10)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(key='w',fun = move_forward)
screen.onkey(key='s',fun = move_backward)
screen.onkey(key='d',fun = rotate_clock)
screen.onkey(key='a',fun = rotate_anticlock)
screen.onkey(key='c',fun = clear_screen)
screen.exitonclick()