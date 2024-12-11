from levels import GameLevels



def initial_game(): 
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