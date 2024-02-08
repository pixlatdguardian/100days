from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # Make sure to lift the pen up before moving
        self.goto(0, 270)
        self.hideturtle()  # Hide the turtle/arrow representation
        self.update_scoreboard()  # Call a method to update the scoreboard text


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 16, 'normal'))

    def update_scoreboard(self):
        self.clear()  # Clear the previous score before writing the new score
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))
