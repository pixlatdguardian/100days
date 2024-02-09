from turtle import Turtle as t


class Paddle(t):
    def __init__(self, x_pos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_pos, y=0)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), y=new_y)
