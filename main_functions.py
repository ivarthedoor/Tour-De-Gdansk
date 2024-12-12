import os
from time import sleep

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def sleep_and_clear(time):
    sleep(time)
    clear()


BOARD_RANGE = (range(1, 31))
PLAYERS_POSITIONS = [0, 0, 0, 0]
PLAYERS_POINTS = [0, 0, 0, 0]