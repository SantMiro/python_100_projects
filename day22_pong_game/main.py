from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


P1_PADDLE_POSITION = (-350,0)
P2_PADDLE_POSITION = (350,0)
Y_LIMIT = 285
MAX_GOALS = 3

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('PONG')
screen.setup(width=800,height=600)

scoreboard = Scoreboard()
p2_paddle = Paddle(P2_PADDLE_POSITION)
p1_paddle = Paddle(P1_PADDLE_POSITION)
ball = Ball()

screen.listen()
screen.onkey(p1_paddle.up,'w')
screen.onkey(p1_paddle.down,'s')
screen.onkey(p2_paddle.up,'Up')
screen.onkey(p2_paddle.down,'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Ball collisions with edges
    if ball.ycor() > Y_LIMIT or ball.ycor() < -Y_LIMIT:
        ball.wall_bounce()

    # Collision with p2 paddle.
    if p2_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    # Collision with p1 paddle.
    if p1_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Ball goes out of bounds
    if ball.xcor() > 370 or ball.xcor() < -370:
        scoreboard.score(ball)
    
    # End game
    if scoreboard.p1_score >= MAX_GOALS or scoreboard.p2_score >= MAX_GOALS:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()