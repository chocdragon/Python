from turtle import Turtle, Screen

# Constants in a class are in capital letters
# each turtle is 20 x 20 pixels
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() # so you can create a method called create_snake
        self.snakehead = self.segments[0]

    def create_snake(self):
        # Loop to create the snake segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        snakey = Turtle("square")
        snakey.color("white")
        snakey.penup()
        snakey.goto(position)
        self.segments.append(snakey)

    def grow_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        # Loop to move the snake starting from it's last segment
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        # Don't forget to move the snake's first segment
        self.snakehead.forward(MOVE_DISTANCE)

    def keyboard_up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)

    def keyboard_left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)

    def keyboard_right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)

    def keyboard_down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)






