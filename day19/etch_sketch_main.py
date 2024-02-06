import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.back(10)


def turn_right():
    tim.right(5)


def turn_left():
    tim.left(5)


def clear_screen():
    tim.setposition(0, 0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
