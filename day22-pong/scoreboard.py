from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()  # Make sure to lift the pen up before moving
        self.goto(0, 270)
        self.hideturtle()  # Hide the turtle/arrow representation
        self.update_scoreboard()  # Call a method to update the scoreboard text



    def update_scoreboard(self):
        self.clear()  # Clear the previous score before writing the new score
        self.write(f"{self.l_score} Score {self.r_score}", align="center", font=('Arial', 16, 'normal'))