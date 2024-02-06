import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="User Bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]
all_turtles = []


for turtle_index in range(6):
    t1 = t.Turtle(shape='turtle')
    t1.color(colors[turtle_index])
    t1.penup()
    t1.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(t1)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The winning color was {winning_color}!")
            else:
                print(f"Sorry, you lost. The winning color was {winning_color}.")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()