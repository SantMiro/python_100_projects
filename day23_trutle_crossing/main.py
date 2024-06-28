from turtle import Turtle, Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.title('Turtle Crossing')
screen.setup(width=600,height=600)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up,'w')
screen.onkey(player.down,'s')



game_on = True
while game_on:
    time.sleep(player.clock_speed)
    screen.update()
    cars.car_manager()
    cars.move_car()


    # Player crosses to the other side
    if player.ycor() > 240:
        time.sleep(1)
        player.level_passed()
        scoreboard.level_passed()

    # Player collides with cars
    for car in cars.car_list:
        if player.distance(car) < 18:
            scoreboard.game_over()
            game_on = False

    
    


    
    

screen.exitonclick()