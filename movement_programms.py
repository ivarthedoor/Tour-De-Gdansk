import random

def throw_the_dice():
    throw = random.randint(1, 1)
    return throw

def move_player(position):
    position += throw_the_dice()
    if position >= 30:  # Zakładając, że plansza ma 30 pól
        position = 29
    return position

# def incorrect_answer():    #-3 pola
# def correct_answer():    #+3 pola