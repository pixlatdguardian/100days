from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            scores = file.read()
            self.high_score = scores
        self.color("white")
        self.penup()  # Make sure to lift the pen up before moving
        self.goto(0, 270)
        self.hideturtle()  # Hide the turtle/arrow representation
        self.update_scoreboard()  # Call a method to update the scoreboard text

    def reset_game(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the previous score before writing the new score
        self.write(f"Score: {self.score} High Score {self.high_score}", align="center", font=('Arial', 16, 'normal'))
