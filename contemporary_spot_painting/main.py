import colorgram
import turtle as tim
import random

# Extract 10 colors from an image.
colors = colorgram.extract('spot_image.jpg', 20)

# This is to format the colorgram extract into a color tuple format (r, g, b)
rgb_choices = [] # Define rgb dictionary
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b) # Create tuple for the r,g b colour
    rgb_choices.append(new_color) # this puts the extracted colors in a tuple format
print(rgb_choices)
# Setting colormode to 255 to allow random color tuple to work
tim.colormode(255)

# Random_colours function to grab one of ten extracted colours from the colorgram tuple
def random_colours():
    mystery = random.randint(0,19)
    print(rgb_choices[mystery])
    return rgb_choices[mystery]

# Setting the coordinate to start from bottom left of the screen
x = -270
y = -200

# hide the turtle arrow
tim.hideturtle()

# Start from bottom left of the screen - coordinate (-250, -200)
while y < 250:
    while x < 300:
        tim.penup()
        start = tim.setpos(x, y)
        tim.pendown()
        tim.dot(20, random_colours())
        x += 60
    y += 60
    x = -270


screen = tim.Screen()
screen.exitonclick()
