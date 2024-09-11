from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)  #stretch is to make the food half usual pixel size
        self.color("orange")
        self.speed("fastest")
        self.random_food()


    def random_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)

