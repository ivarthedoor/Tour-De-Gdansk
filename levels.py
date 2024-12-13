from core import GameCore
from board import GameBoard
from data_adding_program import CsvWriter
from time import sleep
from movement_programms import move_player
from utiles import sleep_and_clear

        
class GameLevels():
    def __init__(self):
        super().__init__()
        self.board = GameBoard()
        self.core = GameCore()

    def level_mechanics(self, district):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.core.questions_assingment(self.board.players_positions[0], 0, district)
            print("Teraz kolej " + self.core.red + " (2)")
            sleep_and_clear(2)
            return True

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.core.questions_assingment(self.board.players_positions[1], 1, district)
            print("Teraz kolej " + self.core.green + " (3)")
            sleep_and_clear(2)
            return True

        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.core.questions_assingment(self.board.players_positions[2], 2, district)
            print("Teraz kolej " + self.core.yellow + " (4)")
            sleep_and_clear(2)
            return True

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.core.questions_assingment(self.board.players_positions[3], 3, district)
            print("Teraz kolej " + self.core.blue + " (1)")
            sleep_and_clear(2)
            return True

        elif play == "q":
            sleep_and_clear(1)
            return False  # Gracz chce zakończyć grę
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            sleep(2)
            return True

    def next_level_movement_mechanics(self):
        if any(pos == 29 for pos in self.board.players_positions):
            print(self.board.generate_board())
            if self.board.players_positions[0] == 29:
                self.core.position_reset()
                self.core.next_level_points(0, 1, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[1] == 29:
                self.core.position_reset()
                self.core.next_level_points(1, 0, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[2] == 29:
                self.core.position_reset()
                self.core.next_level_points(2, 1, 0, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[3] == 29:
                self.core.position_reset()
                self.core.next_level_points(3, 0, 1, 2)
                sleep_and_clear(0.01)
                return True

    def game1(self):
        while True:
            print("...Stare miasto...\n\n")
            self.core.make_players()
            print(f"START.{self.board.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")
            # Poruszanie się graczem: 
            if not self.level_mechanics("Stare miasto"):
                return False
            if self.next_level_movement_mechanics():
                return True


    def game2(self): 
        while True:
            print("...Stare przedmieście...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_mechanics("Stare Przedmieście"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def game3(self):
        while True:
            print("...Oliwa...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_mechanics("Oliwa"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def game4(self):
        while True:
            print("...Wrzeszcz...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {self.board.generate_board()}.META\n")

            if not self.level_mechanics("Wrzeszcz"):
                return False

            if any(pos == 29 for pos in self.board.players_positions):
                print(self.board.generate_board())
                winner_index = self.board.players_positions.index(29)
                self.core.position_reset()
                self.core.next_level_points(winner_index, *[i for i in range(4) if i != winner_index])
                sleep_and_clear(0.01)
                self.core.end_game_and_save()
                for i in self.core.player_data:
                    print(i)
                return False
            






            # if any(pos == 29 for pos in self.players_positions): # Przenoszenie wszystkich graczy do następnej dzielnicy w momencie kiedy jeden z graczy dotarł do końca pierwszej dzielnicy
            #     print(f"{GameBoard.generate_board()}\n\n")
            #     scores = {"\U0001F535": self.players_points[0], "\U0001F534": self.players_points[1], "\U0001F7E2": self.players_points[2], "\U0001F7E1": self.players_points[3]}
            #     print(scores)
            #     if self.players_positions[0] == 29:
            #         print("Player A wins!")
            #     elif self.players_positions[1] == 29:
            #         print("Player B wins!")
            #     elif self.players_positions[2] == 29:
            #         print("Player C wins!")
            #     elif self.players_positions[3] == 29:
            #         print("Player D wins!")
            #     sleep_and_clear(10)
            #     break