from turtle import Turtle, colormode
import random
tim=Turtle()

colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

tim.pensize(15)
tim.speed("fastest")
direction=[0,90,180,270]
for _ in range(200):
    tim.forward(20)
    tim.color(random_color())
    tim.setheading(random.choice(direction))
