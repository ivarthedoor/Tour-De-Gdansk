from main_functions import sleep_and_clear, BOARD_RANGE
from questions_reading import questions_dispenser

# players_positions = [0, 0, 0, 0]
# task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
# players_points = [0, 0, 0, 0]
class GameCore:
    def __init__(self):
        self.players_positions = [0, 0, 0, 0]
        self.task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
        self.players_points = [0, 0, 0, 0]


    def position_reset(self): 
        """Resets pl pos"""
        self.players_positions[0] = 0
        self.players_positions[1] = 0
        self.players_positions[2] = 0
        self.players_positions[3] = 0

    def next_level_points(self, a: int, b: int, c: int, d: int):
        self.players_points[a] += 15
        self.players_points[b] += 5
        self.players_points[c] += 5
        self.players_points[d] += 5

    def questions_assingment(self, position: int, points_index: int, district: str)->int:  # Losowanie pytania co piąte pole 
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

    def make_players(self): # Generowanie graczy - ale jeszcze bez wyboru  ich ilosći 
        players = [x for x in enumerate(["Blue", "Red","Green", "Yellow"], start=1)]
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            players_list = a, b
            players_board = players_list, self.players_points[i]
            print(f"{players_list[0]}.{players_list[1]}: {self.players_points[i]}")

