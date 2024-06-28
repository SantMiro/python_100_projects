from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

LIMIT = 285

screen = Screen()
screen.tracer(0)    
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')


snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Collision with food
    if snake.squares[0].distance(food) < 17:
        food.refresh()
        scoreboard.score_point()
        snake.increase_size()

    if snake.squares[0].xcor() > LIMIT or snake.squares[0].xcor() < -LIMIT or snake.squares[0].ycor() > LIMIT or snake.squares[0].ycor() < -LIMIT:
        scoreboard.reset()
        snake.reset()

    for square in snake.squares[1:]:
        if snake.squares[0].distance(square) < 10:
            #game_on = False
            scoreboard.reset()
            snake.reset()
            


screen.exitonclick()