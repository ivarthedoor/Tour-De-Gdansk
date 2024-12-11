from main_functions import BOARD_RANGE, PLAYERS_POSITIONS
# from core import GameCore
class GameBoard():

    def get_player_nickname():
        blue = ['\U0001F535', input("Wprowadź nazwę niebieskiego gracza: ")]
        red = ['\U0001F534', input("Wprowadź nazwę czerwonego gracza: ")]
        green = ['\U0001F7E2', input("Wprowadź nazwę zielonego gracza: ")]
        yellow = ['\U0001F7E1', input("Wprowadź nazwę żółtego gracza: ")]
        return " ".join(blue), " ".join(red), " ".join(green), " ".join(yellow)
    
    def generate_board(self):
        board_field = ["____" for _ in BOARD_RANGE] 
        player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"] # ID znaków - kulki określające graczy
        
        for i, position in enumerate(PLAYERS_POSITIONS):
            if board_field[position] == "____":
                board_field[position] = player_symbols[i]
            else:
                board_field[position] += player_symbols[i]

        for i in range(len(board_field)):
            if len(board_field[i]) < 4:
                board_field[i] = board_field[i].ljust(4, '_')

        return ".".join(board_field)
    
