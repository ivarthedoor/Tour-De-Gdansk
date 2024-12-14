from levels import GameLevels
from utils import sleep_and_clear

sleep_and_clear(0)

def initial_game(): 
    print("Witaj w grze Tour De Gdańsk! Zapraszamy do wspólnej zabawy i nauki")
    sleep_and_clear(4)
    game = GameLevels()
    while True:
        if not game.level_1():
            break
        if not game.level_2():
            break
        if not game.level_3():
            break
        if not game.level_4():
            break
        if not game.finish():
            break

initial_game()

print("Koniec")