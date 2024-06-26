from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= 'Make your bet',prompt='Which turtle will win? Pick a color: ')
colors = ['purple','blue','green','gold','orange','red']
turtles = []

y=100
for i in range(6):    
    t1 = Turtle(shape='turtle')
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-230,y=y)
    y-=40
    turtles.append(t1)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() >= 220:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f'You win! The {winner} turtle was the winner of the race.')
            else:
                print(f'You lose. The {winner} turtle was the winner of the race.')
            is_race_on = False 

    
screen.exitonclick()











screen.exitonclick()