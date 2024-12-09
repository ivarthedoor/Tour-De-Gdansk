import random


def throw_the_dice(): 
    throw = random.randint(1, 6) # docelowo 1, 6
    return throw



def move_player(position):
    position += throw_the_dice()
    if position >= 30:
        position = 29 # Zapobiega wyjściu poza plansze w momencie wyrzucenia większej ilości oczek niż pozostało do końca dzielnicy lub mety 
    return position


