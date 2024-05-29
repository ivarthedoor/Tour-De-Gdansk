from core import game1, game2

def initial_game(): 
    while True:
        if not game1():
            break
        if not game2():
            break

initial_game()

print("Koniec")