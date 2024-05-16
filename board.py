import random

def throw_the_dice():
    throw = random.randint(1, 6)
    return throw

board_range = range(1, 100)
position_A = 0
position_B = 0

def positioning_A():
    global position_A
    position_A += throw_the_dice()

def positioning_B():
    global position_B
    position_B += throw_the_dice()

def generate_board():
    board_list = ["____" for i in board_range]
    board_list[position_A - 1] = "A"
    board_list[position_B - 1] = "B"
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