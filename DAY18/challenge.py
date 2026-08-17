from turtle import Turtle
import random
tim=Turtle()

#angela yuu code
colors = [
    "light blue",
    "sky blue",
    "turquoise",
    "plum",
    "lavender",
    "light green",
    "salmon",
    "peach puff"
]

def draw_shape(num_sides):
    angle= 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_sides_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides_n)



#my code 
# tim.shape("turtle")
# #for triangle
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
# #for square 
# tim.color("red")  
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# #for pentagon
# tim.color("green")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
# #for hexagon
# tim.color("pink")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
# #for heptagon
# tim.color("orange")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.42)
# #for octagon
# tim.color("blue")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
# #for nonagon
# tim.color("brown")
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
# #for decagon
# tim.color("voilet")
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)


