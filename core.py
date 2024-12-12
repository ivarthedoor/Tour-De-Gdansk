from main_functions import sleep_and_clear, BOARD_RANGE, PLAYERS_POSITIONS, PLAYERS_POINTS
from questions_reading import questions_dispenser

class GameCore():
    def __init__(self):
        # Pobranie nazw graczy
        # self.players_positions = [0, 0, 0, 0]
        self.task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
        self.blue = (f"\U0001F535 - {input("Wprowadź nazwę niebieskiego gracza: ")}")
        self.red = (f"\U0001F534 - {input("Wprowadź nazwę czerwonego gracza: ")}")
        self.green = (f"\U0001F7E2 - {input("Wprowadź nazwę zielonego gracza: ")}")
        self.yellow = (f"\U0001F7E1 - {input("Wprowadź nazwę żółtego gracza: ")}")
        self.player_data = None
        sleep_and_clear(1)
    
    def position_reset(self): 
    #Reset player position po przekroczeniu granicy dzielnic
        PLAYERS_POSITIONS[0] = 0
        PLAYERS_POSITIONS[1] = 0
        PLAYERS_POSITIONS[2] = 0
        PLAYERS_POSITIONS[3] = 0

    def next_level_points(self, a: int, b: int, c: int, d: int):
    # Punktacja graczy za poprawną odpowiedź 
        PLAYERS_POINTS[a] += 15
        PLAYERS_POINTS[b] += 5
        PLAYERS_POINTS[c] += 5
        PLAYERS_POINTS[d] += 5

    def questions_assingment(self, position: int, points_index: int, district: str)->int:  
    # Losowanie pytania co piąte pole 
        for i in self.task_assingment_positions:
            if position == i:
                if questions_dispenser(district):
                    sleep_and_clear(3)
                    PLAYERS_POINTS[points_index] += 10
                else:
                    sleep_and_clear(3)
                    if PLAYERS_POINTS[points_index] != 0:
                        PLAYERS_POINTS[points_index] -= 5
        return PLAYERS_POINTS[points_index]
    
    def make_players(self): 
    # Generowanie graczy 
        players = [x for x in enumerate([self.blue, self.red, self.green, self.yellow], start=1)]
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            players_list = a, b
            self.player_data = (f"{players_list[0]}.{players_list[1]}: {PLAYERS_POINTS[i]}\n")
            print(f"{players_list[0]}.{players_list[1]}: {PLAYERS_POINTS[i]}\n")
        self.player_data = [players_list[1], PLAYERS_POINTS[i]]
        return self.player_data
            
