import os
from time import sleep
from questions import abcd_questions

class Clearing_terminal:
    def clear():
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

class Clearing_and_waiting:
    def sleep_and_clear(time):
        sleep(time)
        Clearing_terminal.clear()

