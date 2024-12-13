from utiles import sleep_and_clear
from questions_reading import questions_dispenser
from board import GameBoard

class GameCore(GameBoard):
    players_list = None
    def __init__(self):
        super().__init__()
        self.task_assingment_positions = [i - 1 for i in self.board_range if i % 5 == 0]
        self.blue = (f"\U0001F535 {input("Wprowadź nazwę niebieskiego gracza: ")}")
        self.red = (f"\U0001F534 {input("Wprowadź nazwę czerwonego gracza: ")}")
        self.green = (f"\U0001F7E2 {input("Wprowadź nazwę zielonego gracza: ")}")
        self.yellow = (f"\U0001F7E1 {input("Wprowadź nazwę żółtego gracza: ")}")
        
        sleep_and_clear(1)
    
    def position_reset(self): 
    #Reset player position po przekroczeniu granicy dzielnic
        self.players_positions[0] = 0
        self.players_positions[1] = 0
        self.players_positions[2] = 0
        self.players_positions[3] = 0

    def next_level_points(self, a: int, b: int, c: int, d: int):
    # Punktacja graczy za poprawną odpowiedź 
        self.players_points[a] += 15
        self.players_points[b] += 5
        self.players_points[c] += 5
        self.players_points[d] += 5

    def questions_assingment(self, position: int, points_index: int, district: str)->int:  
    # Losowanie pytania co piąte pole 
        for i in self.task_assingment_positions:
            if position == i:
                if questions_dispenser(district):
                    sleep_and_clear(3)
                    self.players_points[points_index] += 10
                else:
                    sleep_and_clear(3)
                    if self.players_points[points_index] != 0:
                        self.players_points[points_index] -= 5
        return self.players_points[points_index]
    
    def make_players(self): 
    # Generowanie graczy 
        players = [x for x in enumerate([self.blue, self.red, self.green, self.yellow], start=1)]
        self.player_data = []
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            points = self.players_points[i]
            self.player_data.append([b, points])
            print(f"{a}.{b}: {points}")
        return self.player_data
            
