class GameBoard():
    players_positions = [0, 0, 0, 0]
    players_points = [0, 0, 0, 0]
    board_range = (range(1, 31))

    def generate_board(self):
        board_field = ["____" for _ in self.board_range] 
        player_symbols = ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"] # niebieski/czerwony/zielony/żółty
        
        for i, position in enumerate(self.players_positions):
            if board_field[position] == "____":
                board_field[position] = player_symbols[i]
            else:
                board_field[position] += player_symbols[i]

        for i in range(len(board_field)):
            if len(board_field[i]) < 4:
                board_field[i] = board_field[i].ljust(4, '_')
                
        return ".".join(board_field)
    
