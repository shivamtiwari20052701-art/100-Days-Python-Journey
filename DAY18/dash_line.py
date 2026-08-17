from turtle import Turtle

tim = Turtle()
tim.color("blue")
tim.shape("turtle")
for _ in range (15):
    tim.forward(20)
    tim.penup()
    tim.forward(8)
    tim.pendown()
    
    