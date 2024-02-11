from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()  # Make sure to lift the pen up before moving
        self.hideturtle()  # Hide the turtle/arrow representation

    def update_scoreboard(self, state, x_y):
        self.score += 1
        self.goto(x_y)
        self.write(f"{state}", align="center", font=('Arial', 16, 'normal'))
