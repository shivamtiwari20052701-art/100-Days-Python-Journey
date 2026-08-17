from turtle import Screen
import time
from snake import Snake
from food import Food 
from scoreboard import Score_Board
snake = Snake()
food = Food()
scoreboard = Score_Board()

# Create the game window
screen = Screen()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
# Turn off automatic screen updates for smooth animation
screen.tracer(0)
game_is_on = True

while game_is_on:

    # Show all movements together
    screen.update()

    # Small delay to control snake speed
    time.sleep(0.1)
    snake.move()

    #Detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall 
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
        

    #Detect collision with tail
    for segment in snake.segments[1:]:#slice the segments list and skip the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
         

screen.exitonclick()