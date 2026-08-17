import turtle
shivu=turtle.Turtle() #here Turtle() is a class and shivu is object of the class 
#or we can do 
#from turtle import Turtle then we have to only write the shivu = Turtle()
print(shivu)
shivu.shape("turtle")
shivu.color("DeepPink")
shivu.forward(100)
my_screen=turtle.Screen()
print(my_screen.canvheight)
#my_screen.exitonclick()