import random
import os
from time import sleep
import questions 
from main_functions import sleep_and_clear
from movement_programms import move_player

board_range = range(1, 31)
position_A = 0
position_B = 0
position_C = 0
position_D = 0

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

task_assingment_positions = [i - 1 for i in board_range if i % 5 == 0]

players_points = [0, 0, 0, 0]
   

def questions_assingment(position, points_index):
    for i in task_assingment_positions:
        if position == i:
            if questions.abcd_questions():
                sleep_and_clear(3)
                players_points[points_index] += 10
            else:
                sleep_and_clear(3)
                if players_points[points_index] != 0:
                    players_points[points_index] -= 5
    return players_points[points_index]

def make_players():
    players = [x for x in enumerate(["Blue", "Red","Green", "Yellow"], start=1)]
    i = 0
    for i in range(len(players)):
        a, b = players[i]
        players_list = a, b
        players_board = players_list, players_points[i]
        print(f"{players_list[0]}.{players_list[1]}: {players_points[i]}")
    

def game1():
    global task_assingment_positions, position_A, position_B, position_C, position_D
    while True:
        make_players()
        print(f"START.{generate_board()} \n \
    ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
        play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            position_A = move_player(position_A)
            questions_assingment(position_A, 0)
            print("Time for Red (2)")
            sleep_and_clear(1)

        elif play == "2":
            position_B = move_player(position_B)
            questions_assingment(position_B, 1)
            print("Time for Green (3)")
            sleep_and_clear(1)

        elif play == "3":
            position_C = move_player(position_C)
            questions_assingment(position_C, 2)
            print("Time for Yellow (4)")
            sleep_and_clear(1)
        elif play == "4":
            position_D = move_player(position_D)
            questions_assingment(position_D, 3)
            print("Time for Blue (1)")
            sleep_and_clear(1)
        elif play == "q":
            sleep_and_clear(1)
            return False
        else:
            print("Invalid input! Please press 1, 2, 3, 4 or q.")

        if position_A == 29 or position_B == 29 or position_C == 29 or position_D == 29:
            print(generate_board())
            if position_A == 29:
                position_A = 0
                position_B = 0
                position_C = 0
                position_D = 0
                players_points[0] += 15
                players_points[1] += 5
                players_points[2] += 5
                players_points[3] += 5
                sleep_and_clear(0.01)
                return True
            elif position_B == 29:
                position_A = 0
                position_B = 0
                position_C = 0
                position_D = 0
                players_points[0] += 5
                players_points[1] += 15
                players_points[2] += 5
                players_points[3] += 5
                sleep_and_clear(0.01)
                return True
            elif position_C == 29:
                position_A = 0
                position_B = 0
                position_C = 0
                position_D = 0
                players_points[0] += 5
                players_points[1] += 5
                players_points[2] += 15
                players_points[3] += 5
                sleep_and_clear(0.01)
                return True
            elif position_D == 29:
                position_A = 0
                position_B = 0
                position_C = 0
                position_D = 0
                players_points[0] += 5
                players_points[1] += 5
                players_points[2] += 5
                players_points[3] += 15
                sleep_and_clear(0.01)
                return True

def game2():
    global task_assingment_positions, position_A, position_B, position_C, position_D

    while True:
        make_players()
        print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
    {generate_board()}.META")
        play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            position_A = move_player(position_A)
            questions_assingment(position_A, 0)
            print("Time for Red (2)")
            sleep_and_clear(1)

        elif play == "2":
            position_B = move_player(position_B)
            questions_assingment(position_B, 1)
            print("Time for Green (3)")
            sleep_and_clear(1)

        elif play == "3":
            position_C = move_player(position_C)
            questions_assingment(position_C, 2)
            print("Time for Yellow (4)")
            sleep_and_clear(1)
        elif play == "4":
            position_D = move_player(position_D)
            questions_assingment(position_D, 3)
            print("Time for Blue (1)")
            sleep_and_clear(1)
        elif play == "q":
            sleep_and_clear(1)
            return False
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
            sleep_and_clear(1)
            return True
        
def initial_game(): 
    while True:
        if not game1():
            break
        if not game2():
            break

initial_game()

print("Koniec")
    