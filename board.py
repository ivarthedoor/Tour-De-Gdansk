#import movement_programms

def board(board_base = None):
    if board_base is None:
        board_base = []
    x = 0
    while x < 10:
        x += 1
        board_base.append(str(x))
    board_lenght = len(board_base)
    empty = ".".join(["____" for characters in board_base])
    return empty

print(board())



def example_player():
    position = 0

def example_district():
    players_position = board()
# plansza = [1, 2, 3, 4]
# print(plansza)
# print()