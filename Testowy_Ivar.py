import random
import os
from time import sleep
import questions 
from main_functions import sleep_and_clear
from movement_programms import move_player

board_range = range(1, 31)
players_positions = [0, 0, 0, 0]

def position_reset(): #Będzie do przeniesienia do movement_programms
    global players_positions
    players_positions[0] = 0
    players_positions[1] = 0
    players_positions[2] = 0
    players_positions[3] = 0

def next_level_points(a, b, c, d): #Będzie do przeniesienia do movement_programms
    players_points[a] += 15
    players_points[b] += 5
    players_points[c] += 5
    players_points[d] += 5


def generate_board():
    global players_positions
    board_field = ["____" for _ in board_range]
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
   

def questions_assingment(position, points_index): #do przeniesienia do questions
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

def make_players(): #do przeniesienia do typing players
    players = [x for x in enumerate(["Blue", "Red","Green", "Yellow"], start=1)]
    i = 0
    for i in range(len(players)):
        a, b = players[i]
        players_list = a, b
        players_board = players_list, players_points[i]
        print(f"{players_list[0]}.{players_list[1]}: {players_points[i]}")
    

def game1(): #zastanawiam się, czy te programy nie powinny się własnie znaleźć w core gry, a sama gra nie powinna być wywoływana np z pliku final_game
    global task_assingment_positions, players_positions
    while True:
        make_players()
        print(f"START.{generate_board()} \n \
    ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
        play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            players_positions[0] = move_player(players_positions[0])
            questions_assingment(players_positions[0], 0)
            print("Time for Red (2)")
            sleep_and_clear(1)

        elif play == "2":
            players_positions[1] = move_player(players_positions[1])
            questions_assingment(players_positions[1], 1)
            print("Time for Green (3)")
            sleep_and_clear(1)

        elif play == "3":
            players_positions[2] = move_player(players_positions[2])
            questions_assingment(players_positions[2], 2)
            print("Time for Yellow (4)")
            sleep_and_clear(1)
        elif play == "4":
            players_positions[3] = move_player(players_positions[3])
            questions_assingment(players_positions[3], 3)
            print("Time for Blue (1)")
            sleep_and_clear(1)
        elif play == "q":
            sleep_and_clear(1)
            return False
        else:
            print("Invalid input! Please press 1, 2, 3, 4 or q.")

        if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29:
            print(generate_board())
            if players_positions[0] == 29:
                position_reset()
                next_level_points(0, 1, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif players_positions[1] == 29:
                position_reset()
                next_level_points(1, 0, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif players_positions[2] == 29:
                position_reset()
                next_level_points(2, 1, 0, 3)
                sleep_and_clear(0.01)
                return True
            elif players_positions[3] == 29:
                position_reset()
                next_level_points(3, 0, 1, 2)
                sleep_and_clear(0.01)
                return True

def game2():
    global task_assingment_positions, players_positions

    while True:
        make_players()
        print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
    {generate_board()}.META")
        play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
        play = play.lower()

        if play == "1":
            players_positions[0] = move_player(players_positions[0])
            questions_assingment(players_positions[0], 0)
            print("Time for Red (2)")
            sleep_and_clear(1)

        elif play == "2":
            players_positions[1] = move_player(players_positions[1])
            questions_assingment(players_positions[1], 1)
            print("Time for Green (3)")
            sleep_and_clear(1)

        elif play == "3":
            players_positions[2] = move_player(players_positions[2])
            questions_assingment(players_positions[2], 2)
            print("Time for Yellow (4)")
            sleep_and_clear(1)
        elif play == "4":
            players_positions[3] = move_player(players_positions[3])
            questions_assingment(players_positions[3], 3)
            print("Time for Blue (1)")
            sleep_and_clear(1)
        elif play == "q":
            sleep_and_clear(1)
            return False
        else:
            print("Invalid input! Please press 1, 2, 3, 4 or q.")

        if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29:
            print(generate_board())
            if players_positions[0] == 29:
                print("Player A wins!")
            elif players_positions[1] == 29:
                print("Player B wins!")
            elif players_positions[2] == 29:
                print("Player C wins!")
            elif players_positions[3] == 29:
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
    