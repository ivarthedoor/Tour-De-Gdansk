from core import GameCore
from board import GameBoard
from time import sleep
from movement_programms import move_player
from utiles import sleep_and_clear

# Z ajkiegoś powodu ostatni ruch gracza (kończońcy grę), nie przyznaje punktów, oraz wyświetla się komunikat ruchu następnego gracz.
# Trzeba to poprawić
class GameLevels(GameCore):
    def __init__(self):
        super().__init__()
        self.board = GameBoard()

    def level_movement_mechanics(self, district: str):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.questions_assingment(self.board.players_positions[0], 0, district)
            print("Teraz kolej " + self.red + " (2)")
            sleep_and_clear(2)
            return True

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.questions_assingment(self.board.players_positions[1], 1, district)
            print("Teraz kolej " + self.green + " (3)")
            sleep_and_clear(2)
            return True

        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.questions_assingment(self.board.players_positions[2], 2, district)
            print("Teraz kolej " + self.yellow + " (4)")
            sleep_and_clear(2)
            return True

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.questions_assingment(self.board.players_positions[3], 3, district)
            print("Teraz kolej " + self.blue + " (1)")
            sleep_and_clear(2)
            return True

        elif play == "q": # Zakończenie gry
            sleep_and_clear(1)
            return False
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            sleep(2)
            return True

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

    def game1(self):
        while True:
            print("...Stare miasto...\n\n")
            self.make_players()
            print(f"START.{self.board.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare miasto"):
                return False
            if self.next_level_movement_mechanics():
                return True


    def game2(self): 
        while True:
            print("...Stare przedmieście...\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare Przedmieście"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def game3(self):
        while True:
            print("...Oliwa...\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Oliwa"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def game4(self):
        while True:
            print("...Wrzeszcz...\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {self.board.generate_board()}.META\n")
            

            play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
            play = play.lower()

            if play == "1":
                self.board.players_positions[0] = move_player(self.board.players_positions[0])
                self.questions_assingment(self.board.players_positions[0], 0, "Wrzeszcz")
                if self.board.players_positions[0] != 29:
                    print("Teraz kolej " + self.red + " (2)")
                sleep_and_clear(2)

            elif play == "2":
                self.board.players_positions[1] = move_player(self.board.players_positions[1])
                self.questions_assingment(self.board.players_positions[1], 1, "Wrzeszcz")
                if self.board.players_positions[1] != 29:
                    print("Teraz kolej " + self.green + " (3)")
                sleep_and_clear(2)

            elif play == "3":
                self.board.players_positions[2] = move_player(self.board.players_positions[2])
                self.questions_assingment(self.board.players_positions[2], 2, "Wrzeszcz")
                if self.board.players_positions[2] != 29:
                    print("Teraz kolej " + self.yellow + " (4)")
                sleep_and_clear(2)

            elif play == "4":
                self.board.players_positions[3] = move_player(self.board.players_positions[3])
                self.questions_assingment(self.board.players_positions[3], 3, "Wrzeszcz")
                if self.board.players_positions[3] != 29:
                    print("Teraz kolej " + self.blue + " (1)")
                sleep_and_clear(2)
                
            

            elif play == "q": # Zakończenie gry
                sleep_and_clear(1)
                # return False
            else:
                print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
                sleep(2)
                # return True
                # if not self.level_movement_mechanics("Wrzeszcz"):
                #     return False

            
            if self.next_level_movement_mechanics():
                # sleep_and_clear(0.01)
                self.end_game_and_save()
                for i in self.player_data:
                    print(i)
                return False






            # if any(pos == 29 for pos in self.board.players_positions):
            #     print(self.board.generate_board())
            #     winner_index = self.board.players_positions.index(29)
            #     self.position_reset()
            #     self.next_level_points(winner_index, *[i for i in range(4) if i != winner_index])
            #     sleep_and_clear(0.01)
            #     self.end_game_and_save()
            #     for i in self.player_data:
            #         print(i)
            #     return False