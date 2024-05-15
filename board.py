x = 0
board_base = []
def board(x):
    while x < 100:
        x += 1
        board_base.append(str(x))
        if x % 10 == 0:
            board_base.append("\n")
board(x)


def clear_gameboard():
    game_board = "|".join(board_base)
    board_lenght = len(game_board)
    empty = ".".join(["_" for characters in game_board])
    print("Nazwa: " + "".join(empty))
clear_gameboard()