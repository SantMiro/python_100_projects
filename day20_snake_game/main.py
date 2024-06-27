from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.tracer(0)    
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')


snake = Snake()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')

screen.update()
game_on = True
while game_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()