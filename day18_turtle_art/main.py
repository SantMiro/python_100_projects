from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('frieren.jpg',20)

screen = Screen()
screen.colormode(255)


def random_color(colors):
    color = random.choice(colors)
    color = color.rgb
    return color

def paint_dots(x,y,dot_size,colors,timmy_the_turtle):
    while x <= size[0]:
        while y >= -size[1]:
            timmy_the_turtle.dot(dot_size,random_color(colors))
            y -= dot_size * 2
            timmy_the_turtle.teleport(x,y)
        x += dot_size * 2
        y = size[1]
        timmy_the_turtle.teleport(x,y)



timmy_the_turtle = Turtle()
timmy_the_turtle.speed('fastest')
timmy_the_turtle.hideturtle()
size = screen.screensize()
timmy_the_turtle.teleport(-size[0]+50,size[1])
dot_size = 20
x = -size[0] + 50
y = size[1]

paint_dots(x,y,dot_size,colors,timmy_the_turtle)




screen.exitonclick()