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

def get_player_name():
    number_players = int(input("Podaj liczbę graczy: "))
    player_name = []
    for names in range(number_players):
        name = input(f"Podaj imię gracza{names + 1}: ")
        player_name.append(name)
    return player_name

name_list = get_player_name()
print("Imiona graczy to: ")
for name in name_list:
    print(name)



