from turtle import Turtle
import random

COLORS = ['violet','blue','green','yellow','orange','red']
CAR_SPEED = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.car_list = []


    def generate_car(self):
        y = random.randint(-200,200)
        car = Turtle(shape='square')
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(250,y)
        car.shapesize(1, 2, 1)
        self.car_list.append(car)


    def move_car(self):
        cars_to_remove = []
        for car in self.car_list:
            new_x = car.xcor() - CAR_SPEED
            car.goto(new_x,car.ycor())
            if car.xcor() < -350:
                cars_to_remove.append(car)
        for car in cars_to_remove:
            car.ht()
            self.car_list.remove(car)
        

    def car_manager(self):
        get_car = random.choice([0, 0, 0, 1])
        if get_car == 1:
            self.generate_car()
            
    

