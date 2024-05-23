# import random

# def throw_the_dice():
#     throw = random.randint(1, 1)
#     return throw

# board_range = range(1, 30)
# position_A = 0
# position_B = 1
# position_C = 1
# position_D = 1
# equal_position = 0


# def positioning_A():
#     global position_A
#     position_A += throw_the_dice()

# def positioning_B():
#     global position_B
#     position_B += throw_the_dice()

# def positioning_C():
#     global position_C
#     position_C += throw_the_dice()



# def generate_board():
#     global position_A
#     global position_B
#     global position_C
#     global equal_position
    
#     board_list = ["____" for _ in board_range]
#     if  position_A != position_B and position_A != position_C and position_B != position_C:
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[position_B - 1] = "_\U0001F534__"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#     elif position_A == position_B and position_A == position_C and position_B == position_C:
#         equal_position = position_A
#         board_list[equal_position - 1] = "_\U0001F535\U0001F534\U0001F7E2"        
#     elif position_A == position_B:
#         equal_position = position_A  
#         board_list[equal_position - 1] = "_\U0001F535\U0001F534_"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#     elif position_A == position_C:
#         equal_position = position_A
#         board_list[position_B - 1] = "_\U0001F534__"
#         board_list[equal_position - 1] = "_\U0001F535\U0001F7E2_"
#     elif position_B == position_C:
#         equal_position = position_B
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[equal_position - 1] = "_\U0001F534\U0001F7E2_"
#     board_joined = ".".join(board_list)
#     return board_joined


# def game():
#     while True:
#         play = input("press a to move A, b to move B, or q to quit: ")
#         if play == "a":
#             positioning_A()
#         elif play == "b":
#             positioning_B()
#         elif play == "c":
#             positioning_C()
#         elif play == "q":
#             break
#         print(generate_board())

# game()

###Przenieś ten cały syf w osobny folder#####


# import random

# def throw_the_dice():
#     throw = random.randint(1, 1)
#     return throw

# board_range = range(1, 30)
# position_A = 0
# position_B = 1
# position_C = 1
# position_D = 1
# equal_position = 0


# def positioning_A():
#     global position_A
#     position_A += throw_the_dice()

# def positioning_B():
#     global position_B
#     position_B += throw_the_dice()

# def positioning_C():
#     global position_C
#     position_C += throw_the_dice()

# def positioning_D():
#     global position_D
#     position_D += throw_the_dice()


# def generate_board():
#     global position_A
#     global position_B
#     global position_C
#     global position_D
#     global equal_position
    
#     board_list = ["____" for _ in board_range]
#     if  position_A != position_B and position_A != position_C and position_B != position_C and position_D != position_A and position_D != position_B and position_D != position_C:
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[position_B - 1] = "_\U0001F534__"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#         board_list[position_D - 1] = "_\U0001F7E1__"
#     elif position_A == position_B and position_A == position_C and position_B == position_C and position_D == position_A and position_D == position_B and position_D == position_C:
#         equal_position = position_A
#         board_list[equal_position - 1] = "_\U0001F535\U0001F534\U0001F7E2\U0001F7E1"        
#     elif position_A == position_B:
#         equal_position = position_A  
#         board_list[equal_position - 1] = "_\U0001F535\U0001F534_"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#         board_list[position_D - 1] = "_\U0001F7E1__"
#     elif position_A == position_C:
#         equal_position = position_A
#         board_list[equal_position - 1] = "_\U0001F535\U0001F7E2_"
#         board_list[position_B - 1] = "_\U0001F534__"
#         board_list[position_D - 1] = "_\U0001F7E1__"
#     elif position_A == position_D:
#         equal_position = position_A  
#         board_list[equal_position - 1] = "_\U0001F535\U0001F7E1_"
#         board_list[position_B - 1] = "_\U0001F534__"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#     elif position_B == position_C:
#         equal_position = position_B
#         board_list[equal_position - 1] = "_\U0001F534\U0001F7E2_"
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[position_D - 1] = "_\U0001F7E1__"
#     elif position_B == position_D:
#         equal_position = position_B
#         board_list[equal_position - 1] = "_\U0001F534\U0001F7E1_"
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[position_C - 1] = "_\U0001F7E2__"
#     elif position_C == position_D:
#         board_list[equal_position - 1] = "_\U0001F7E2\U0001F7E1_"
#         board_list[position_A - 1] = "_\U0001F535__"
#         board_list[position_B - 1] = "_\U0001F534__"
#     elif position_A == position_B == position_C:
#         board_list[equal_position - 1] = "_\U0001F535\U0001F534\U0001F7E2_"
#         board_list[position_D - 1] = "_\U0001F7E1__"

#     board_joined = ".".join(board_list)
#     return board_joined


# def game():
#     while True:
#         play = input("press a to move A, b to move B, c to move C, d to move D or q to quit: ")
#         if play == "a":
#             positioning_A()
#         elif play == "b":
#             positioning_B()
#         elif play == "c":
#             positioning_C()
#         elif play == "d":
#             positioning_D()
#         elif play == "q":
#             break
#         print(generate_board())

# game()




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
