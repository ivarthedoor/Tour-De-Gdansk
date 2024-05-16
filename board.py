import random

def throw_the_dice():
    throw = random.randint(1, 6)
    return throw

board_range = range(1, 30)
position_A = 0
position_B = 1
equal_position = 0


def positioning_A():
    global position_A
    position_A += throw_the_dice()

def positioning_B():
    global position_B
    position_B += throw_the_dice()


def generate_board():
    global position_A
    global position_B
    global equal_position
    
    board_list = ["____" for _ in board_range]
    if position_A != position_B:
        board_list[position_A - 1] = "_A__"
        board_list[position_B - 1] = "_B__"
    elif position_A == position_B:
        equal_position = position_A  
        board_list[equal_position] = "_AB_"  
    board_joined = ".".join(board_list)
    return board_joined


def game():
    while True:
        play = input("press a to move A, b to move B, or q to quit: ")
        if play == "a":
            positioning_A()
        elif play == "b":
            positioning_B()
        elif play == "q":
            break
        print(generate_board())

game()