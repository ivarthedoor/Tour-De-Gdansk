from levels import GameLevels
from core import GameCore



def initial_game(): 
    game = GameLevels()
    core = GameCore()
    core.get_player_nickname()

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