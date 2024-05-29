import random

def throw_the_dice():
    throw = random.randint(1, 1) # docelowo 1, 6
    return throw

def move_player(position):
    position += throw_the_dice()
    if position >= 30:
        position = 29
    return position


