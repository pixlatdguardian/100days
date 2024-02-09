import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True


def reset_ball():
    time.sleep(0.5)
    ball.velocity = 0.1
    ball.reset()


while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect paddle misses
    if ball.xcor() > 395:
        reset_ball()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
    elif ball.xcor() < -395:
        reset_ball()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
