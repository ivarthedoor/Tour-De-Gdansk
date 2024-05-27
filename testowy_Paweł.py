import random
from time import sleep


# def clear():
#     if os.name == "posix":
#         os.system("clear")
#     else:
#         os.system("cls")

# def sleep_and_clear(time):
#     sleep(time)
#     clear()

# funkcja rzutu kością
# def roll_the_dice():
#     return random.randint(1,6)

# print(roll_the_dice())

# przedstawienie się i naciśij enter, aby rzucić kością


# funkcja uzyskania liczby graczy i podania ich imion

# def get_player_name():
#     number_players = int(input("Podaj liczbę graczy: "))
#     player_name = []
#     for names in range(number_players):
#         name = input(f"Podaj imię gracza{names + 1}: ")
#         player_name.append(name)
#     return player_name

# name_list = get_player_name()
# print("Imiona graczy to: ")
# for name in name_list:
#     print(name)


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
#     global position_A, position_B, position_C, position_D
    
#     board_list = ["____" for _ in board_range]
#     players_positions = [position_A, position_B, position_C, position_D]
#     player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"]
    
#     for i, position in enumerate(players_positions):
#         if board_list[position - 1] == "____":
#             board_list[position - 1] = ""
#         board_list[position - 1] += player_symbols[i]
    
#     board_joined = ""
#     for symbol in board_list:
#         if symbol == "____":
#             board_joined += "____."
#         else:
#             board_joined += f"_{symbol}__."
    
#     return board_joined.rstrip(".")


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



# # for symbol in board_list:
# #     if symbol == "____":
# #         board_joined += "____."
# #     else:
# #         board_joined += f"{symbol}."

import random
import os
from time import sleep
import questions
          
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

def move_player(position):
    position += throw_the_dice()
    if position >= 30:  # Zakładając, że plansza ma 30 pól
        position = 29
    return position

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

    for i in range(len(board_field)):
        if len(board_field[i]) < 4:
            board_field[i] = board_field[i].ljust(4, '_')

    return ".".join(board_field)


task_assingment_positions = []
for i in board_range:
    if i % 5 == 0:
        task_assingment_positions.append(i - 1)

players_points = [0, 0, 0, 0]
   

def questions_assingment(position, points_index):
    for i in task_assingment_positions:
        if position == i:
            if questions.abcd_questions():
                sleep_and_clear(3)
                players_points[points_index] += 10
            else:
                sleep_and_clear(3)
                players_points[points_index] -= 5
    return players_points[points_index]

def game():
    global task_assingment_positions, position_A, position_B, position_C, position_D
   
    while True:
        print(f"A: {players_points[0]}")
        print(f"B: {players_points[1]}")
        print(f"C: {players_points[2]}")
        print(f"D: {players_points[3]}")
        print(generate_board())
        play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            position_A = move_player(position_A)
            questions_assingment(position_A, 0)
            sleep_and_clear(0.1)

        elif play == "2":
            position_B = move_player(position_B)
            questions_assingment(position_B, 1)
            sleep_and_clear(0.1)

        elif play == "3":
            position_C = move_player(position_C)
            questions_assingment(position_C, 2)
            sleep_and_clear(0.1)
        elif play == "4":
            position_D = move_player(position_D)
            questions_assingment(position_D, 3)
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

