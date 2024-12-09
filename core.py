from main_functions import sleep_and_clear, BOARD_RANGE, PLAYERS_POSITIONS
from questions_reading import questions_dispenser

class GameCore():
    def __init__(self):
        # Pobranie nazw graczy
        # self.players_positions = [0, 0, 0, 0]
        self.task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
        self.players_points = [0, 0, 0, 0]
        self.blue = (f"\U0001F535 - {input("Wprowadź nazwę niebieskiego gracza: ")}")
        self.red = (f"\U0001F534 - {input("Wprowadź nazwę czerwonego gracza: ")}")
        self.green = (f"\U0001F7E2 - {input("Wprowadź nazwę zielonego gracza: ")}")
        self.yellow = (f"\U0001F7E1 - {input("Wprowadź nazwę żółtego gracza: ")}")
        sleep_and_clear(1)
    
    def position_reset(self): 
    #Reset player position po przekroczeniu granicy dzielnic
        PLAYERS_POSITIONS[0] = 0
        PLAYERS_POSITIONS[1] = 0
        PLAYERS_POSITIONS[2] = 0
        PLAYERS_POSITIONS[3] = 0

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
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            players_list = a, b
            print(f"{players_list[0]}.{players_list[1]}: {self.players_points[i]}\n")
