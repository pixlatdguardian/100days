import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle = Player()
car_list = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkeypress(turtle.move, "Up")

car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_counter += 1
    car_list.move_cars()
    if car_counter == 6:
        car_list.create_car()
        car_counter = 0

    for car in car_list.all_cars:
        if turtle.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    # FinishLine
    if turtle.ycor() > 280:
        car_list.level_up()
        turtle.start_over()
        scoreboard.score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()