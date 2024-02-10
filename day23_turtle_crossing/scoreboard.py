from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()  # Make sure to lift the pen up before moving
        self.goto(0, 260)
        self.hideturtle()  # Hide the turtle/arrow representation
        self.update_scoreboard()  # Call a method to update the scoreboard text

    def update_scoreboard(self):
        self.clear()  # Clear the previous score before writing the new score
        self.write(f" Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" GAME OVER. Score {self.score}", align="center", font=FONT)
