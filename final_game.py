from levels import GameLevels
from board import GameBoard



def initial_game(): 
    game = GameLevels()
    board = GameBoard

    board.get_player_nickname()
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