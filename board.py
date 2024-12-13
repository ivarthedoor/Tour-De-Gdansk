from utiles import BOARD_RANGE
class GameBoard():
    players_positions = [0, 0, 0, 0]
    players_points = [0, 0, 0, 0]

    def generate_board(self):
        board_field = ["____" for _ in BOARD_RANGE] 
        player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"] # ID znaków - kulki określające graczy
        
        for i, position in enumerate(self.players_positions):
            if board_field[position] == "____":
                board_field[position] = player_symbols[i]
            else:
                board_field[position] += player_symbols[i]

        for i in range(len(board_field)):
            if len(board_field[i]) < 4:
                board_field[i] = board_field[i].ljust(4, '_')
                
        return ".".join(board_field)
    
