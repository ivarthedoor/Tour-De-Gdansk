from core import game1, game2, game3, game4

def initial_game(): 
    while True:
        if not game1():
            break
        if not game2():
            break
        if not game3():
            break
        if not game4():
            break

initial_game() # Włączenie gry poprzez funkcję, która wywołuje po kolei dzielnice

print("Koniec")