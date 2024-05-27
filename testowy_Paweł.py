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


