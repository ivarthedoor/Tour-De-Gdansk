import os
from time import sleep
from questions import abcd_questions

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def sleep_and_clear(time):
    sleep(time)
    clear()


BOARD_RANGE = (range(1, 31))