from datetime import datetime
from board import GameBoard
from data_adding_program import CsvWriter
from utils import sleep_and_clear
from questions_reading import GameQuestions


class GameCore(GameBoard):
    csv_writer = CsvWriter()
    questions_disp = GameQuestions()
    def __init__(self):
        self.task_assingment_positions = [i - 1 for i in self.board_range if i % 3 == 0]
    # Nadanie nazw przez użytkowników
        self.blue = (f"\U0001F535 {input("Wprowadź nazwę niebieskiego gracza: ")}")
        self.red = (f"\U0001F534 {input("Wprowadź nazwę czerwonego gracza: ")}")
        self.green = (f"\U0001F7E2 {input("Wprowadź nazwę zielonego gracza: ")}")
        self.yellow = (f"\U0001F7E1 {input("Wprowadź nazwę żółtego gracza: ")}")
        
        sleep_and_clear(1)
    
    def position_reset(self)->int: 
    # Po przekroczeniu granicy dzielnic
        self.players_positions[0] = 0
        self.players_positions[1] = 0
        self.players_positions[2] = 0
        self.players_positions[3] = 0

    def next_level_points(self, a: int, b: int, c: int, d: int):
        self.players_points[a] += 15
        self.players_points[b] += 5
        self.players_points[c] += 5
        self.players_points[d] += 5

    def points_for_questions(self, position: int, points_index: int, district: str):  
    # Pytanie przypisane jest co piąte pole 
        for i in self.task_assingment_positions:
            if position == i:
                if self.questions_disp.questions_dispenser(district):
                    self.players_points[points_index] += 10
                else:
                    if self.players_points[points_index] != 0:
                        self.players_points[points_index] -= 5
        return self.players_points[points_index]
    
    def make_players(self)->list:
        players = [x for x in enumerate([self.blue, self.red, self.green, self.yellow], start=1)]
        actual_date = datetime.now()
        formatted_actual_date = actual_date.strftime("%Y-%m-%d %H:%M")
        self.player_data = []
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            points = self.players_points[i]
            self.player_data.append([str(formatted_actual_date), str(b), points])
            print(f"{a}.{b}: {points}")
        return self.player_data

    def end_game_and_save(self):
        for player in self.player_data:
            self.csv_writer.write_to_csv(player)
        self.csv_writer.sort_csv_by_column()