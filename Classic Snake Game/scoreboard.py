from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Tahoma", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self, mark):
        super().__init__()


    def tally(self, mark):
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("yellow")
        self.write(f"Score: {mark}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


