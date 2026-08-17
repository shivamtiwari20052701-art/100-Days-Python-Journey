from turtle import Turtle
# Starting positions of the 3 snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create each snake segment
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()          # So it doesn't draw lines
        new_segment.goto(position)   # Place the segment at its starting position
        self.segments.append(new_segment) # Add the segment to the list
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake from back to front
            # Last segment copies the position of the segment in front of it
            for seg_num in range(len(self.segments) - 1, 0, -1):
                # for seg_num in range(start=2,stop=0,step=-1) -> this is not valid Python syntax, I wrote it only to understand that start=2, stop=0 and step=-1. The actual Python code is range(2,0,-1).
                new_x = self.segments[seg_num - 1].xcor()  # x-coordinate of previous segment
                new_y = self.segments[seg_num - 1].ycor()  # y-coordinate of previous segment
        
                # Move current segment to previous segment's position
                self.segments[seg_num].goto(new_x, new_y)
        
            # Finally move the head forward
            self.head.forward(MOVE_DISTANCE)

            #note:# We move from the last segment to the first.
            # If we move from front to back, every segment would copy
            # the already moved position and the snake won't move correctly.

    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
           self.head.setheading(DOWN)   

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    