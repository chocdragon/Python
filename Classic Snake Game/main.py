from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

point = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard(point)

screen.listen()
screen.onkey(snake.keyboard_up, "Up")
screen.onkey(snake.keyboard_down, "Down")
screen.onkey(snake.keyboard_left, "Left")
screen.onkey(snake.keyboard_right, "Right")


play = True

while play:
    screen.update() # Update the screen after all segments have moved
    time.sleep(0.2)
    snake.move()
    score.tally(point)

    # Detect if snake touches the food using turtle distance
    if snake.snakehead.distance(food) < 15: # If distance snake to food is 12 pixels apart, we can assume it will collide
        food.random_food() #regenerate the food in other random spot
        score.clear()
        point += 1
        snake.grow_snake() #grow snake body length everytime it eats

    # Detect if snake hits the wall, then game over
    if snake.snakehead.xcor() > 290 or snake.snakehead.xcor() < -290 or snake.snakehead.ycor() > 270 or snake.snakehead.ycor() < -290:
        play = False
        score.game_over()

    # Detect if snake collides with itself, then game over too
    for body in snake.segments[1:]:
        if snake.snakehead.distance(body) <10:
            play = False
            score.game_over()
#       Alternative method to detect snake collision with itself
#        if body == snake.snakehead:
#            pass
#        if snake.snakehead.distance(body) < 10:
#            play = False
#            score.game_over()





screen.exitonclick()
