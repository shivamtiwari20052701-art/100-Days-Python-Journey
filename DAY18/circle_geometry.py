from turtle import Turtle,Screen,colormode
import random 

tim=Turtle()
colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
#tim.pensize(2)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)#will change the heading of the turtle
draw_spirograph(3)
screen=Screen() 
screen.exitonclick() 