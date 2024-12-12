from levels import GameLevels
from utiles import sleep_and_clear

sleep_and_clear(0)

def initial_game(): 
    # print("Witaj w grze Tour De Gdańsk! Zapraszamy do wspólnej zabawy i nauki")
    # sleep_and_clear(4)
    game = GameLevels()
    while True:
        if not game.game1():
            break
        if not game.game2():
            break
        if not game.game3():
            break
        if not game.game4():
            break

initial_game()

print("Koniec")