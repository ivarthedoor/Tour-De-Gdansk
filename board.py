import random

def throw_the_dice():
    throw = random.randint(1, 1)
    return throw

board_range = range(1, 30)
position_A = 0
position_B = 1
position_C = 1
position_D = 1
equal_position = 0


def positioning_A():
    global position_A
    position_A += throw_the_dice()

def positioning_B():
    global position_B
    position_B += throw_the_dice()

def positioning_C():
    global position_C
    position_C += throw_the_dice()

def positioning_D():
    global position_D
    position_D += throw_the_dice()


def generate_board():
    global position_A, position_B, position_C, position_D
    
    board_list = ["____" for _ in board_range]
    players_positions = [position_A, position_B, position_C, position_D]
    player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"]
    
    for i, position in enumerate(players_positions):
        if board_list[position - 1] == "____":
            board_list[position - 1] = ""
        board_list[position - 1] += player_symbols[i]
    
    board_joined = ""
    for symbol in board_list:
        if symbol == "____":
            board_joined += "____."
        else:
            board_joined += f"_{symbol}__."
    
    return board_joined.rstrip(".")

import questions
task_assingment_positions = []
for i in board_range:
    if i % 5 == 0:
        task_assingment_positions.append(i)


def game():
    while True:
        play = input("press a to move A, b to move B, c to move C, d to move D or q to quit: ")
        if play == "a":
            positioning_A()
        elif play == "b":
            positioning_B()
        elif play == "c":
            positioning_C()
        elif play == "d":
            positioning_D()
        elif play == "q":
            break
        print(generate_board())

game()


##
##