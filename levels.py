from core import GameCore
from board import GameBoard
from movement_programms import move_player
from utils import sleep_and_clear

class GameLevels(GameCore):
    def __init__(self):
        super().__init__()
        self.board = GameBoard()

    def level_movement_mechanics(self, district: str):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.points_for_questions(self.board.players_positions[0], 0, district)
            print("Teraz kolej " + self.red + " (2)")
            return True, sleep_and_clear(3)

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.points_for_questions(self.board.players_positions[1], 1, district)
            print("Teraz kolej " + self.green + " (3)")
            return True, sleep_and_clear(3)
            
        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.points_for_questions(self.board.players_positions[2], 2, district)
            print("Teraz kolej " + self.yellow + " (4)")
            return True, sleep_and_clear(3)

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.points_for_questions(self.board.players_positions[3], 3, district)
            print("Teraz kolej " + self.blue + " (1)")
            return True, sleep_and_clear(3)

        elif play == "q":
            sleep_and_clear(3)
            return False
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            return True, sleep_and_clear(3)

    def final_level_movement_mechanics(self, district: str):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.points_for_questions(self.board.players_positions[0], 0, district)
            if self.board.players_positions[0] != 29:
                print("Teraz kolej " + self.red + " (2)")
            return True, sleep_and_clear(3)

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.points_for_questions(self.board.players_positions[1], 1, district)
            if self.board.players_positions[1] != 29:
                print("Teraz kolej " + self.green + " (3)")
            return True, sleep_and_clear(3)
            
        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.points_for_questions(self.board.players_positions[2], 2, district)
            if self.board.players_positions[2] != 29:
                print("Teraz kolej " + self.yellow + " (4)")
            return True, sleep_and_clear(3)

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.points_for_questions(self.board.players_positions[3], 3, district)
            if self.board.players_positions[3] != 29:
                print("Teraz kolej " + self.blue + " (1)")
            return True, sleep_and_clear(3)

        elif play == "q":
            sleep_and_clear(3)
            return False
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            return True, sleep_and_clear(3)

    def next_level_movement_mechanics(self)->bool:
        if any(pos == 29 for pos in self.board.players_positions):
            print(self.board.generate_board())
            if self.board.players_positions[0] == 29:
                self.position_reset()
                self.next_level_points(0, 1, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[1] == 29:
                self.position_reset()
                self.next_level_points(1, 0, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[2] == 29:
                self.position_reset()
                self.next_level_points(2, 1, 0, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[3] == 29:
                self.position_reset()
                self.next_level_points(3, 0, 1, 2)
                sleep_and_clear(0.01)
                return True

    def level_1(self):
        while True:
            print("...Stare Miasto...\n\n")
            self.make_players()
            print(f"\nSTART.{self.board.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare Miasto"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_2(self): 
        while True:
            print("...Stare Przedmieście...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare Przedmieście"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_3(self):
        while True:
            print("...Oliwa...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Oliwa"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_4(self):
        while True:
            print("...Wrzeszcz...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {self.board.generate_board()}.META\n")

            if not self.final_level_movement_mechanics("Wrzeszcz"):
                return False
            if self.next_level_movement_mechanics():
                return True
            
    def finish(self):
        self.make_players()
        sleep_and_clear(0)
        self.end_game_and_save()
        for i in self.player_data:
            print(i)
        return False