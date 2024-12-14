
from core import game1, game2
from questions import abcd_questions
from utils import sleep_and_clear
from board import board_range, generate_board
from movement_programms import move_player


players_positions = [0, 0, 0, 0]
task_assingment_positions = [i - 1 for i in board_range if i % 5 == 0]
players_points = [0, 0, 0, 0]


def position_reset():
    global players_positions
    players_positions[0] = 0
    players_positions[1] = 0
    players_positions[2] = 0
    players_positions[3] = 0

def next_level_points(a, b, c, d):
    players_points[a] += 15
    players_points[b] += 5
    players_points[c] += 5
    players_points[d] += 5

def questions_assingment(position, points_index):
    for i in task_assingment_positions:
        if position == i:
            if abcd_questions():
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

def game3():
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
        if not game3():
            break

initial_game()

print("Koniec")











































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


