from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.horizontal_movement = 10
        self.vertical_movement = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.horizontal_movement
        new_y = self.ycor() + self.vertical_movement
        self.goto(new_x,new_y)

    def bounce_vertical(self):
        #reverse the direction
        self.vertical_movement *= -1

    def bounce_horizontal(self):
        self.horizontal_movement *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1 
        self.bounce_horizontal()


