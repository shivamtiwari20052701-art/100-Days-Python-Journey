from  turtle import Turtle,Screen,colormode
import random
colormode(255)
tim=Turtle()
screen=Screen()
#import colorgram
#extrat colors from the image
#colors=colorgram.extract('C:/Users/shyam/OneDrive/Desktop/100_days_python/DAY18/project/image.jpg',30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# print(rgb_colors)
#now remove the baground color which is white
 
color_list=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=101
tim.speed("fastest")

for dots in range(1, num_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.forward(30)

    if dots%10==0:
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)

   
    

screen.exitonclick()
