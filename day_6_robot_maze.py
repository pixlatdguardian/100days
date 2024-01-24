#This is for use in the Reeborg's World challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def navigate():
    if front_is_clear():
        move()
        if not wall_on_right():
            turn_right()
    elif wall_on_right() and not wall_in_front():
        move()
    else:
        turn_left()
while front_is_clear():
    move()
        
while not at_goal():
    navigate()