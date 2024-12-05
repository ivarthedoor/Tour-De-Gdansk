from core import Game_levels

def initial_game(): 
    while True:
        if not Game_levels.game1():
            break
        if not Game_levels.game2():
            break
        if not Game_levels.game3():
            break
        if not Game_levels.game4():
            break

initial_game() # Włączenie gry poprzez funkcję, która wywołuje po kolei dzielnice

print("Koniec")