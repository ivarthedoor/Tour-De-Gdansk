import random
import os
from time import sleep
import questions


# board_range = range(1, 30)
# position_A = 0
# position_B = 1
# position_C = 2
# position_D = 3
# equal_position = 0

# def generate_board():
#     global position_A, position_B, position_C, position_D
#     for characters in board_range:
#         board_fields = ['_' for players_field in range(4)] 
#         board_fields.append(board_fields)
#         # board_numbers = []
#     # number = 0
#     # for numbers in range(30):
#     #     number += 1
#     #     board_numbers.append(str(number))
    
#     board_fields[position_A] = "\U0001F535"
#     board_fields[position_B] = "\U0001F534"
#     board_fields[position_C] = "\U0001F7E2"
#     board_fields[position_D] = "\U0001F7E1"
#     print(board_fields)
#     # print(f"Plansza: {" ".join(board_fields)}")
#     # print(f"Plansza: {" ".join(board_numbers)}")
#     players_positions = [position_A, position_B, position_C, position_D]
#     player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"]
    
#     # for i, position in enumerate(players_positions):
#     #     if board_field[position - 1] == "____":
#     #         board_list[position - 1] = ""
#     #     board_list[position - 1] += player_symbols[i]
    
#     # board_joined = ""
#     # for symbol in board_list:
#     #     if symbol == "____":
#     #         board_joined += "____."
#     #     else:
#     #         board_joined += f"_{symbol}__."
    
#     # return board_joined.rstrip(".")

# generate_board()

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def sleep_and_clear(time):
    sleep(time)
    clear()

def throw_the_dice():
    throw = random.randint(1, 1)
    return throw

board_range = range(1, 28)
position_A = 0
position_B = 0
position_C = 0
position_D = 0
# equal_position = 0
def move_player(position):
    position += throw_the_dice()
    if position >= 30:  # Zakładając, że plansza ma 30 pól
        position = 29
    return position

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


def generate_board():
    global position_A, position_B, position_C, position_D
    
    board_field = ["____" for _ in board_range]
    players_positions = [position_A, position_B, position_C, position_D]
    player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"]
    
    for i, position in enumerate(players_positions):
        if board_field[position] == "____":
            board_field[position] = player_symbols[i]
        else:
            board_field[position] += player_symbols[i]

        # Upewnij się, że każda pozycja na planszy ma dokładnie 4 znaki
    for i in range(len(board_field)):
        if len(board_field[i]) < 4:
            board_field[i] = board_field[i].ljust(4, '_')

    return ".".join(board_field)
    
    # board_joined = ""
    # for symbol in board_field:
    #     if symbol == "____":
    #         board_joined += "____."
    #     else:
    #         board_joined += f"_{symbol}__."
    
    # return board_joined.rstrip(".")


task_assingment_positions = []
for i in board_range:
    if i % 5 == 0:
        task_assingment_positions.append(i - 1)

def questions_assingment(x):
    # global player_A_points
    for i in task_assingment_positions:
        if x == i:
            questions.abcd_questions()
            sleep(3)
            clear()
            # if questions.abcd_questions == True:
            #     player_A_points = player_A_points + 10
            #     # position_A + 10
            #     # print(f"Player A {player_A_points}")
            # else:
            #     player_A_points = player_A_points - 10
            #     # position_A - 10
            #     # print(f"Player A {player_A_points}")


def game():
    global position_A, position_B, position_C, position_D

    
    while True:
        print(generate_board())
        play = input("press a to move Blue, b to move Red, c to move Green, d to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            position_A = move_player(position_A)
            questions_assingment(position_A)
            sleep_and_clear(0.1)
        elif play == "2":
            position_B = move_player(position_B)
            sleep_and_clear(0.1)
        elif play == "3":
            position_C = move_player(position_C)
            sleep_and_clear(0.1)
        elif play == "4":
            position_D = move_player(position_D)
            sleep_and_clear(0.1)
        elif play == "q":
            sleep_and_clear(0.1)
            break
        else:
            print("Invalid input! Please press 1, 2, 3, 4 or q.")

        if position_A == 29 or position_B == 29 or position_C == 29 or position_D == 29:
            print(generate_board())
            if position_A == 29:
                print("Player A wins!")
            elif position_B == 29:
                print("Player B wins!")
            elif position_C == 29:
                print("Player C wins!")
            elif position_D == 29:
                print("Player D wins!")
            break


game()

