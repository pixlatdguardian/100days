import turtle
import pandas as pd
from score import Scoreboard

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
correct_guess = []
game_is_on = True

# score = Scoreboard()
score = Scoreboard()

while game_is_on:
    answer_state = screen.textinput(title=f"You have {score.score}/50 states.", prompt="What is the name of a state?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in correct_guess]
        break
    for index, row in data.iterrows():
        if row['state'] == answer_state:
            # Pull x, y data for the matching state
            x_y = (row['x'], row['y'])
            score.update_scoreboard(answer_state, x_y)
            correct_guess.append(answer_state)
    if len(correct_guess) == 50:
        game_is_on = False

study = pd.DataFrame(missed_states)
study.to_csv("states_to_learn.csv")
