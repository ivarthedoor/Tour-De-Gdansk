from core import GameLevels

def initial_game(): 
    while True:
        if not GameLevels.game1():
            break
        if not GameLevels.game2():
            break
        if not GameLevels.game3():
            break
        if not GameLevels.game4():
            break

initial_game() # Włączenie gry poprzez funkcję, która wywołuje po kolei dzielnice

print("Koniec")